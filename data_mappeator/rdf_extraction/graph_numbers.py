import os
from conf.config import parser
from MyGraph import MyGraph

output_directory = parser.get('files', 'output_directory')
os.chdir(os.path.dirname(__file__))
file_id_map = []

print("Loading the articles info...")
g = MyGraph(parser.get('files', 'input'))

qarticles = g.get_all_article_ids()
num_articles = len(qarticles)
print("The number of articles parsed is: %i" % (num_articles))

qprocesses = g.get_num_processes()
num_processes = len(qprocesses)
print("The number of phoyocatalytic processes parsed is: %i" % (num_processes))

num_elements = g.get_num_elements()
for row in num_elements:
    print("The number of instances parsed is: %s" % (row.triples))

num_properties = g.get_num_properties()
for row in num_properties:
    print("The number of triplets parsed is: %s" % (row.properties))