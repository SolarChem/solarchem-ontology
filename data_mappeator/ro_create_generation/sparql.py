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
    qconstruct = graph.query(get_article_rdf_query(iri))
    filename = parser.get('files', 'output_name')+"_"+doi
    filedir = parser.get('files', 'output_directory')+"/"+filename+".rdf"
    qconstruct.serialize(filedir)

def get_article_rdf_query(iri) -> str:
    return """
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX phcat: <http://base.namespace.com/>

        CONSTRUCT { 
            <%s> ?article_prop ?article_val . 
            ?journal ?journal_prop ?journal_val .
            ?creator ?creator_prop ?creator_val .
            ?country ?country_prop ?country_val .
            ?mat_trans ?mat_trans_prop ?mat_trans_val .
            ?yield ?yield_prop ?yield_val .
            ?eg ?eg_prop ?eg_val .
            ?bet ?bet_prop ?bet_val .
            ?condition ?condition_prop ?condition_val .
            ?input ?input_prop ?input_val .
            ?output ?output_prop ?output_val .
            ?chem_in ?chem_in_prop ?chem_in_val .
            ?chem_out ?chem_out_prop ?chem_out_val .
            ?output_q ?output_q_prop ?output_q_val .
        }
        WHERE { 
            <%s> ?article_prop ?article_val ;
                 dcterms:isPartOf  ?journal ;
                 dcterms:creator   ?creator ;
                 phcat:hasMaterialTransformationProcess ?mat_trans .

            ?journal ?journal_prop ?journal_val .

            ?creator ?creator_prop ?creator_val .

            ?mat_trans ?mat_trans_prop ?mat_trans_val ;
                       phcat:hasInput ?input ;
                       phcat:hasOutput ?output .
            
            ?input ?input_prop ?input_val ;
                   phcat:hasChemical ?chem_in .

            ?output ?output_prop ?output_val ;
                    phcat:hasOutputQuantity ?output_q ;
                    phcat:hasChemical ?chem_out .

            ?chem_in ?chem_in_prop ?chem_in_val .
            ?chem_out ?chem_out_prop ?chem_out_val .
            ?output_q ?output_q_prop ?output_q_val .

            OPTIONAL { 
                ?creator phcat:affiliationCountry ?country . 
                ?country ?country_prop ?country_val .

                ?mat_trans phcat:hasYield ?yield ;
                           phcat:hasReactionEg ?eg ;
                           phcat:hasBET ?bet ;
                           phcat:hasCondition ?condition .

                ?yield ?yield_prop ?yield_val .
                ?eg ?eg_prop ?eg_val .
                ?bet ?bet_prop ?bet_val .
                ?condition ?condition_prop ?condition_val .
            }
        }
    """ % (iri, iri)

def load_graph():
    g = rdflib.Graph()
    g.parse(parser.get('files', 'input'), format="turtle")
    return g