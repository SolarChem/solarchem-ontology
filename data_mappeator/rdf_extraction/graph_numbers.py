import os
from conf.config import parser
from MyGraph import MyGraph

output_directory = parser.get('files', 'output_directory')
os.chdir(os.path.dirname(__file__))
file_id_map = []

print("Loading the articles info...")
g = MyGraph(parser.get('files', 'input'))

print("Geting all the URIs...")
qarticles = g.get_all_article_ids()

num_articles = len(qarticles)
print("The number of articles parsed is: %i" % (num_articles))

num_elements = g.get_num_elements()
for row in num_elements:
    print("The number of triplets parsed is: %s" % (row.triples))

num_properties = g.get_num_properties()
for row in num_properties:
    print("The number of properties parsed is: %s" % (row.properties))