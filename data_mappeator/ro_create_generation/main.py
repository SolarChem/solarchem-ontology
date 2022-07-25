import os
from conf.config import parser
from utils import *
from MyGraph import MyGraph

output_directory = parser.get('files', 'output_directory')
os.chdir(os.path.dirname(__file__))

print("Cleaning the articles folder...")
clean_directory(output_directory)

print("Loading the articles info...")
g = MyGraph(parser.get('files', 'input'))

print("Geting all the URIs...")
qarticles = g.get_all_article_iris()

print("Generating new RDF files...")
for row in qarticles: 
    article_graph = g.create_article_rdf(row.individual) # row.individual = article iri
    article_graph.serialize(get_file_directory_name(row.individual))

list = os.listdir(output_directory) # dir is your directory path
number_files = len(list)
print("Number of created files: "+str(number_files))