import os
from conf.config import parser
from utils import *
from MyGraph import MyGraph
from colorama import Fore, Style
import csv

output_directory = parser.get('files', 'output_directory')
os.chdir(os.path.dirname(__file__))
file_id_map = []

# print("Cleaning the articles folder...")
# clean_directory(output_directory)

print("Loading the articles info...")
g = MyGraph(parser.get('files', 'input'))

print("Geting all the URIs...")
qarticles = g.get_all_article_ids()

print("Generating RDF files...")
for row in qarticles:
    doi = row.doi
    try:
        article_graph = g.create_article_rdf(row.individual) # row.individual = article iri
        file_dir = get_file_directory_name(doi)
        article_graph.serialize(file_dir)
        file_id_map.append({'DOI': doi, 'file': get_filename(doi)})
    except Exception:
        print(f"\tError in: {Fore.RED}{doi}{Style.RESET_ALL}\n")


file_list = os.listdir(output_directory) # dir is your directory path
number_files = len(file_list)
print(f"Number of created files: {Fore.BLUE}{str(number_files)}{Style.RESET_ALL}")

print("Creating mapping file...")
fieldnames = list(file_id_map[0].keys())
with open(parser.get('files', 'map_file'), 'w', errors='surrogatepass', encoding="utf8", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(file_id_map)

print("PROCESS FINISHED.")