from db_connect import cursor
from utils import *
import re
import pycountry

def prepare_from_query(query):
    cursor.execute(query)

    result = cursor.fetchall()
    for i in range(len(result)):
        result[i] = clean_row(result[i])

    return result

def prepare_articles(limit = -1):
    query = """SELECT p.*, j.ID as journalID FROM paper_references p, journals j 
        WHERE j.name = p.Journal AND No_de_Ref IN (SELECT No_de_Ref FROM catalystsdata)
    """
    if limit > 0:
        query = query + " LIMIT " + str(limit)

    return prepare_from_query(query)

def prepare_journals(articles):
    result = {}
    for article in articles:
        journal_id = article['journalID']
        if not journal_id in result:
            journal = {'ID': journal_id,
                'name': article['Journal']
                }

            result[journal_id] = journal

    return list(result.values())

def prepare_authors(articles):
    name_regex = '\*\s*'
    split_regex = ",\s*"
    result = []
    for article in articles:
        article_id = article['ID']
        author_names = re.split(split_regex, article['Authors'])
        countries = re.split(split_regex, article['Country'])
        corresponding_mail = article['Corresponding_author']
        mail_referenced = False
        first_author_pos = len(result)

        for i in range(len(author_names)):
            author_id = len(result)+1
            aname = author_names[i]
            email = None

            if aname != '':
                if re.search(name_regex, aname):
                    aname = re.sub(name_regex, '', aname)
                    if not mail_referenced:
                        # NOTE: esto no es correcto, habria que preguntar cual es la 
                        #       mejor forma de relacionar el mail con el author
                        mail_referenced = True
                        email = corresponding_mail

                c, cname = prepare_countries(countries, i)
                
                author = {'ID': author_id,
                    'paperID': article_id,
                    'name': aname,
                    'email': email,
                    'country': c,
                    'country_name': cname
                    }
                
                result.append(author)
        
        if not mail_referenced and len(result) >= first_author_pos:
            result[first_author_pos]['email'] = corresponding_mail

    return result

def prepare_countries(countries, i):
    c = None 
    cname = None

    if len(countries) > i:
        country = pycountry.countries.get(alpha_2=countries[i])
        if country:
            c = country.alpha_2
            cname = country.name
    
    return c, cname

def prepare_material_transformations(articles = None):
    query = "SELECT * FROM catalystsdata"
    if articles:
        paper_refs = []
        for article in articles:
            paper_refs.append(str(article['No_de_Ref'])) #primero se transforma a string para evitar errores al unir el texto

        joined_list = ",".join(paper_refs)
        query_aux = " WHERE No_de_Ref IN (" + joined_list + ");"
        query = query + query_aux

    return prepare_from_query(query)

def prepare_inputs(mtplist):
    result = []
    for mtp in mtplist:
        # input format => ['chemical', percentage]
        input_list = {
            'Catalyst': [mtp['Catalyst'], None],
            'Support': [mtp['Support'], mtp['support_percent']],
            'Co-catalyst_1': [mtp['Co_catalyst'], mtp['percent']],
            'Co-catalyst_2': [mtp['co_catalyst_2'], mtp['percent_cc_2']],
            'Co-catalyst_3': [mtp['co_catalyst_3'], mtp['percent_cc_3']],
            'Dopant': [mtp['Dopant'], mtp['dopant_percent']],
            'Dye': [mtp['Dyes'], mtp['dye_percent']],
            'Reductant': [mtp['Reductant'], None]
        }

        for input_id in input_list:
            input = input_list[input_id]
            # if the first element (chemical) is not None then exists and we add the role and append
            if input[0]:
                if 'Co-catalyst' in input_id:
                    input_id = 'Co-catalyst'

                result.append({'ID': len(result)+1,
                    'Material_transformation_id': mtp['ID'],
                    'Chemical': input[0],
                    'Percent': input[1],
                    'Role': input_id,
                    'crystal_structure': mtp['TiO2_crystal_structure']
                })
                
    return result

def prepare_conditions(mtplist):
    result = []
    for mtp in mtplist:
        cond_list = {
            'ReactorCondition': [mtp['Reactor_type'], mtp['Reactor_Volume_l'], 'L'],
            'CatalystSetUpCondition': [mtp['Catalyst_set_up'], mtp['Masscat_g'], 'GM'],
            'LampPowerCondition': [mtp['Lamp'], mtp['Power_W'], 'W'],
            'LampIrradianceCondition': [mtp['Lamp'], mtp['Light_Intensity_W_m2'], 'W-PER-M2'],
            'TemperatureCondition': [None, mtp['T_C'], 'DEG_C'],
            'PreasureCondition': [None, mtp['P_bar'], 'BAR'],
            'SpaceVelocityCondition': [None, mtp['Residence_time_min1'], 'PER-HR'],
            'ReactionTimeCondition': [None, mtp['Reaction_time_h'], 'HR'],
            'ReactionMediumCondition': [mtp['Reaction_medium'], mtp['ph_value'], 'PH'],
            'WavelengthCondition': [mtp['Light_source'], mtp['Wavelength_nm'], 'NanoM'],
            'IlluminatedAreaCondition': [mtp['Light_source'], mtp['Illuminated_area_m2'], 'M2']
        }
        
        for cond_id in cond_list:
            cond = cond_list[cond_id]
            if not check_if_all_none(cond):
                condition = {'ID': len(result)+1,
                    'Material_transformation_id': mtp['ID'],
                    'Type': cond[0],
                    'Quantity': None,
                    'Numeric_quantity': cond[1],
                    'Condition': cond_id,
                    'Reactor_type': None,
                    'Set_up_type': None,
                    'Lamp_type': None,
                    'Reaction_medium_type': None,
                    'Light_source_type': None,
                    'QUDT_unit': cond[2]
                }

                if cond_id == 'ReactorCondition':
                    condition['Reactor_type'] = cond[0]
                elif cond_id == 'CatalystSetUpCondition':
                    condition['Set_up_type'] = cond[0]
                elif cond_id == 'LampPowerCondition' or cond_id == 'LampIrradianceCondition':
                    condition['Lamp_type'] = cond[0]
                elif cond_id == 'ReactionMediumCondition':
                    condition['Reaction_medium_type'] = cond[0]
                elif cond_id == 'IlluminatedAreaCondition':
                    condition['Light_source_type'] = cond[0]
                elif cond_id == 'WavelengthCondition':
                    condition['Light_source_type'] = cond[0]
                    condition['Quantity'] = condition['Numeric_quantity']
                    condition['Quantity'] = None
                
                result.append(condition)

    return result

def prepare_outputs(mtplist):
    unit_equivalences = {'g': 'MicroMOL-PER-GM', 
        'gh': 'MicroMOL-PER-GM-HR', 
        'm2h': 'MicroMOL-PER-M2-HR'
    }
    result = []
    for mtp in mtplist:
        keylist = mtp.keys()
        for key in keylist:
            if '_mol_' in key:
                splited_key = key.split('_')
                chemical = splited_key[0]
                unit = splited_key[-1]
                quantity = mtp[key]
                if quantity is not None and quantity > 0:
                    result.append({'ID': len(result)+1,
                    'Material_transformation_id': mtp['ID'],
                    'Chemical': chemical,
                    'Quantity': quantity,
                    'Unit': unit,
                    'QUDT_unit': unit_equivalences[unit]
                })
    return result

def prepare_chemicals(itemlits):
    result = []
    chem_list = []
    for item in itemlits:
        chem = item['Chemical']
        if not chem in chem_list:
            chem_list.append(chem)
            result.append({'ID': len(result)+1,
                'Chemical': chem
            })

    return result

def prepare_units(itemlist):
    result = [{'ID': 1, 'Unit': 'EV'}, {'ID': 2, 'Unit': 'M2-PER-GM'}]
    unit_list = []
    for unit in result:
        unit_list.append(unit['Unit'])

    for item in itemlist:
        unit = item['QUDT_unit']
        if not unit in unit_list:
            unit_list.append(unit)
            result.append({'ID': len(result)+1,
                'Unit': unit
            })

    return result
