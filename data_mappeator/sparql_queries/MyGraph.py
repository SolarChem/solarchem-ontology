from rdflib import Graph
from queries import *
from const import *

class MyGraph:

    def __init__(self, filename):
        self.__graph = Graph()
        self.__graph.parse(filename, format="turtle")

    def get_processes_by_year(self):
        return self.__graph.query(processes_by_year())

    def get_processes_by_country(self):
        return self.__graph.query(processes_by_country())

    def get_processes_by_catalyst(self):
        return self.__graph.query(processes_by_catalyst())

    def get_articles_from_journal(self, journal, year = None, volume = None):
        return self.__graph.query(articles_from_journal(journal, year, volume))


