def query_select_all_articles() -> str:
    return """
            PREFIX bibo: <http://purl.org/ontology/bibo/>

            SELECT ?individual ?doi
            WHERE { ?individual a bibo:Article ;
                                bibo:doi ?doi . }
        """

def query_construct_article(iri) -> str:
    return """
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX phcat: <http://base.namespace.com/>

        CONSTRUCT { 
            <%s> ?article_prop ?article_val . 
            ?journal ?journal_prop ?journal_val .
            ?creator ?creator_prop ?creator_val .
            ?country ?country_prop ?country_val .
        }
        WHERE { 
            <%s> ?article_prop ?article_val ;
                 dcterms:isPartOf  ?journal ;
                 dcterms:creator   ?creator .

            ?journal ?journal_prop ?journal_val .
            ?creator ?creator_prop ?creator_val .

            OPTIONAL { 
                ?creator phcat:affiliationCountry ?country . 
                ?country ?country_prop ?country_val .
            }
        }
    """ % (iri, iri)

def query_construct_material_transformation(iri) -> str:
    return """
            PREFIX phcat: <http://base.namespace.com/>

            CONSTRUCT { 
                ?mat_trans ?mat_trans_prop ?mat_trans_val .
                ?yield ?yield_prop ?yield_val .
                ?eg ?eg_prop ?eg_val .
                ?bet ?bet_prop ?bet_val .
            }
            WHERE { 
                ?mat_trans ?mat_trans_prop ?mat_trans_val ;
                    phcat:reportedIn <%s> .

                OPTIONAL { 
                    ?mat_trans phcat:hasYield ?yield ;
                            phcat:hasReactionEg ?eg ;
                            phcat:hasBET ?bet .

                    ?yield ?yield_prop ?yield_val .
                    ?eg ?eg_prop ?eg_val .
                    ?bet ?bet_prop ?bet_val .
                }
            }
        """ % (iri)

def query_construct_input_output(iri)->str:
    return """
            PREFIX phcat: <http://base.namespace.com/>

            CONSTRUCT { 
                ?input ?input_prop ?input_val .
                ?output ?output_prop ?output_val .
                ?chem_in ?chem_in_prop ?chem_in_val .
                ?chem_out ?chem_out_prop ?chem_out_val .
                ?output_q ?output_q_prop ?output_q_val .
            }
            WHERE { 
                ?mat_trans phcat:hasInput ?input ;
                    phcat:hasOutput ?output ;
                    phcat:reportedIn <%s> .

                ?input ?input_prop ?input_val ;
                   phcat:hasChemical ?chem_in .

                ?output ?output_prop ?output_val ;
                    phcat:hasOutputQuantity ?output_q ;
                    phcat:hasChemical ?chem_out .

                ?chem_in ?chem_in_prop ?chem_in_val .
                ?chem_out ?chem_out_prop ?chem_out_val .
                ?output_q ?output_q_prop ?output_q_val .
            }
        """ % (iri)

def query_construct_condition(iri) -> str:
    return """
            PREFIX phcat: <http://base.namespace.com/>

            CONSTRUCT { ?condition ?condition_prop ?condition_val . }
            WHERE { 
                ?mat_trans phcat:reportedIn <%s> .

                OPTIONAL { 
                    ?mat_trans phcat:hasCondition ?condition .
                    ?condition ?condition_prop ?condition_val .
                }
            }
        """ % (iri)

def query_select_count_elements() -> str:
    return """SELECT (COUNT(?s) AS ?triples) WHERE { ?s a ?o }"""

def query_select_count_properties() -> str:
    return """SELECT (COUNT(?p) AS ?properties) WHERE { ?s ?p ?o }"""