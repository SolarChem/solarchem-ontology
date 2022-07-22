from conf.config import parser
import rdflib

def get_all_article_iris(graph):
    query = """
        PREFIX bibo: <http://purl.org/ontology/bibo/>

        SELECT ?individual
        WHERE { ?individual a bibo:Article . }
    """
    return graph.query(query) # get all the article instances

def create_article_rdf(graph, iri):
    doi = iri.split("/")[-1]

    query = """
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX phcat: <http://base.namespace.com/>

        CONSTRUCT { 
            <%s> ?article_property ?article_value . 
            ?journal ?journal_property ?journal_value .
            ?creator ?creator_property ?creator_value .
            ?country ?country_property ?country_value .
        }
        WHERE { 
            <%s> ?article_property ?article_value ;
                 dcterms:isPartOf  ?journal ;
                 dcterms:creator   ?creator ;
                 phcat:hasMaterialTransformationProcess ?mat_trans .

                ?journal ?journal_property ?journal_value .

                ?creator ?creator_property ?creator_value .

                OPTIONAL { ?creator phcat:affiliationCountry ?country . 
                           ?country ?country_property ?country_value .
                }
        }
    """ % (iri, iri)

    qconstruct = graph.query(query)
    filename = parser.get('files', 'output_name')+"_"+doi
    filedir = parser.get('files', 'output_directory')+"/"+filename+".rdf"
    qconstruct.serialize(filedir)

def load_graph():
    g = rdflib.Graph()
    g.parse(parser.get('files', 'input'), format="turtle")
    return g

