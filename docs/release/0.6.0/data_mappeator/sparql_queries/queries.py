## This file contains explained SPARQL queries taht are used to filter the dataset

def processes_by_year() -> str:
    return """
    PREFIX phcat: <http://base.namespace.com/>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?year (COUNT(DISTINCT ?mat_trans) AS ?num_process)
    WHERE { ?individual phcat:hasMaterialTransformationProcess ?mat_trans ;
                        dcterms:date ?year . }
    GROUP BY ?year
    """

def processes_by_country() -> str:
    return """
    PREFIX phcat: <http://base.namespace.com/>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?country (COUNT(DISTINCT ?mat_trans) AS ?num_process)
    WHERE { 
        ?individual phcat:hasMaterialTransformationProcess ?mat_trans ;
                    dcterms:creator ?creator .
        ?creator phcat:affiliationCountry ?country .
    }
    GROUP BY ?country
    """

def processes_by_catalyst() -> str:
    return """
    PREFIX phcat: <http://base.namespace.com/>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?catalyst (COUNT(DISTINCT ?mat_trans) AS ?num_process)
    WHERE { 
        ?mat_trans phcat:hasInput ?input .
        ?input phcat:hasChemical ?chem ;
            phcat:hasRole 
    <http://base.namespace.com/Catalyst> .
        ?chem rdfs:label ?catalyst.
    }
    GROUP BY ?catalyst
    """

def articles_from_journal(journal, year = None, volume = None) -> str:
    year_filter = ""
    volume_filter = ""
    if year:
        year_filter = "dcterms:date <%s> ;" % (year)
        if volume:
            volume_filter = "bibo:volume <%s> ;" % volume
    
    query = """
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX dcterms: <http://purl.org/dc/terms/>

    SELECT ?article
    WHERE { ?article <%s>
                     <%s>
                     dcterms:isPartOf ?journal . 

            ?journal dcterms:title <%s> .
    }
    """ % (year_filter, volume_filter, journal)

    return query

def processes_by_input_and_output(role = None, 
input_chem = None, 
conditon = None, 
condition_value = None,
output_chem = None):

    if role:
        role_filter_mat_trans = "phcat:hasInput ?input "
        role_filter = """?input phcat:hasRole <%s> ;
            phcat:hasChemical ?chemin .
            ?chemin rdfs:label "<%s>" .  
        """ % (role, input_chem)
        if not (conditon and output_chem):
            role_filter_mat_trans = role_filter_mat_trans + '.'
        else:
            role_filter_mat_trans = role_filter_mat_trans + ';'
    
    if conditon:
        condition_filter_mat_trans = "phcat:hasCondition ?condition ;"
        conditon_filter = "?condition phcat:<%s> <%s> ." % (conditon, condition_value)
        if not (output_chem):
            condition_filter_mat_trans = condition_filter_mat_trans + '.'
        else:
            condition_filter_mat_trans = condition_filter_mat_trans + ';'
    
    if output_chem:
        output_filter_mat_trans = "phcat:hasOutput ?output ."
        output_filter = """?output phcat:hasChemical ?chemout .
            ?chemout rdfs:label "<%s>" .  
        """ % (output_chem)

    query = """
    PREFIX phcat: <http://base.namespace.com/>
    PREFIX qudt: <http://qudt.org/2.1/schema/qudt/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?mat_trans
    WHERE { 
        ?mat_trans <%s>
                <%s>
                <%s>
        <%s>  
        <%s>
        <%s>
    }
    """ % (role_filter_mat_trans, 
    condition_filter_mat_trans,
    output_filter_mat_trans,
    role_filter,
    conditon_filter,
    output_filter)

    return query

def processes_by_input_and_output_ordered_by_output_cant(output_chem,
output_unit,
role = None, 
input_chem = None, 
conditon = None, 
condition_value = None):

    if role:
        role_filter_mat_trans = "phcat:hasInput ?input "
        role_filter = """?input phcat:hasRole <%s> ;
            phcat:hasChemical ?chemin .
            ?chemin rdfs:label "<%s>" .  
        """ % (role, input_chem)
        if not (conditon and output_chem):
            role_filter_mat_trans = role_filter_mat_trans + '.'
        else:
            role_filter_mat_trans = role_filter_mat_trans + ';'
    
    if conditon:
        condition_filter_mat_trans = "phcat:hasCondition ?condition ;"
        conditon_filter = "?condition phcat:<%s> <%s> ." % (conditon, condition_value)
        if not (output_chem):
            condition_filter_mat_trans = condition_filter_mat_trans + '.'
        else:
            condition_filter_mat_trans = condition_filter_mat_trans + ';'

    query = """
    PREFIX phcat: <http://base.namespace.com/>
    PREFIX qudt: <http://qudt.org/2.1/schema/qudt/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?mat_trans ?chemout ?outquan_val
    WHERE { 
        ?mat_trans <%s>
                <%s>
                phcat:hasOutput ?output .
        <%s>  
        <%s>
        ?output phcat:hasChemical ?chemout .
        ?chemout rdfs:label "<%s>" ;
            phcat:hasOutputQuantity ?outquan .
        ?outquan qudt:numericValue ?outquan_val ;
            qudt:unit <%s> .
    }
    """ % (role_filter_mat_trans, 
    condition_filter_mat_trans,
    role_filter,
    conditon_filter,
    output_chem,
    output_unit)

    return query