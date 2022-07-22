import os
from sparql import *
from conf.config import parser
from utils import clean_directory

output_directory = parser.get('files', 'output_directory')
os.chdir(os.path.dirname(__file__))

print("Cleaning the articles folder...")
clean_directory(output_directory)

print("Loading the articles info...")
g = load_graph()

print("Geting all the URIs...")
qarticles = get_all_article_iris(g)

print("Generating new RDF files...")
for row in qarticles:
    create_article_rdf(g, row.individual)

list = os.listdir(output_directory) # dir is your directory path
number_files = len(list)
print("Number of created files: "+str(number_files))