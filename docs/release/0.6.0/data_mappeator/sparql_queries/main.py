import os
from conf.config import parser
from MyGraph import MyGraph
from colorama import Fore, Style

os.chdir(os.path.dirname(__file__))

print("Loading the articles info...")
g = MyGraph(parser.get('files', 'input'))

processes_by_year = g.get_processes_by_year()
print(processes_by_year.serialize(format='json'))

print("PROCESS FINISHED.")