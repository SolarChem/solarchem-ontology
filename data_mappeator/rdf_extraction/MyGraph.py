from rdflib import Graph
from sparql import *

class MyGraph:

    def __init__(self, filename):
        self.__graph = Graph()
        self.__graph.parse(filename, format="turtle")

    def get_all_article_ids(self):
        return self.__graph.query(query_select_all_articles()) # get all the article instances


    def create_article_rdf(self, iri):
        g_article = Graph()
        g_material_trans_process = Graph()
        g_input_output = Graph()
        g_condition = Graph()

        r_article = self.__graph.query(query_construct_article(iri))
        r_material_trans_process = self.__graph.query(query_construct_material_transformation(iri))
        r_input_output = self.__graph.query(query_construct_input_output(iri))
        r_condition = self.__graph.query(query_construct_condition(iri))

        g_article.parse(r_article.serialize(), format="xml")
        g_material_trans_process.parse(r_material_trans_process.serialize(), format="xml")
        g_input_output.parse(r_input_output.serialize(), format="xml")
        g_condition.parse(r_condition.serialize(), format="xml")

        result_graph = g_article + g_material_trans_process + g_input_output + g_condition
        return result_graph

    def get_num_elements(self):
        return self.__graph.query(query_select_count_elements())

    def get_num_properties(self):
        return self.__graph.query(query_select_count_properties())