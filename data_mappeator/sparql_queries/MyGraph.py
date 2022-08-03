from rdflib import Graph

class MyGraph:

    def __init__(self, filename):
        self.__graph = Graph()
        self.__graph.parse(filename, format="turtle")

    def get_processes_by_year(self):
        query = """
            PREFIX phcat: <http://base.namespace.com/>
            PREFIX dcterms: <http://purl.org/dc/terms/>

            SELECT ?year (COUNT(DISTINCT ?mat_trans) AS ?num_process)
            WHERE { ?individual phcat:hasMaterialTransformationProcess ?mat_trans ;
                                dcterms:date ?year . }
            GROUP BY ?year
        """
        return self.__graph.query(query)


