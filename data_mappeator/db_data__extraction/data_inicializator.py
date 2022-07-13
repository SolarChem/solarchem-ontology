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

def prepare_articles():
    query = "SELECT p.*, j.ID as journalID FROM paper_references p, journals j WHERE j.name = p.Journal"
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

def prepare_material_transformations():
    query = "SELECT * FROM catalystsdata"
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
            'Reactor_condition': [mtp['Reactor_type'], mtp['Reactor_Volume_l'], 'L'],
            'Catalyst_set_up_condition': [mtp['Catalyst_set_up'], mtp['Masscat_g'], 'GM'],
            'Lamp_power_condition': [mtp['Lamp'], mtp['Power_W'], 'W'],
            'Lamp_irradiance_condition': [mtp['Lamp'], mtp['Light_Intensity_W_m2'], 'W-PER-M2'],
            'Temperature_condition': [None, mtp['T_C'], 'DEG_C'],
            'Preasure_condition': [None, mtp['P_bar'], 'BAR'],
            'Space_velocity_condition': [None, mtp['Residence_time_min1'], 'PER-HR'],
            'Reaction_time_condition': [None, mtp['Reaction_time_h'], 'HR'],
            'Reaction_medium_condition': [mtp['Reaction_medium'], mtp['ph_value'], 'PH'],
            'Wavelength_condition': [mtp['Light_source'], mtp['Wavelength_nm'], 'NanoM'],
            'Illuminated_area_condition': [mtp['Light_source'], mtp['Illuminated_area_m2'], 'M2']
        }
        
        for cond_id in cond_list:
            cond = cond_list[cond_id]
            if not check_if_all_none(cond):
                result.append({'ID': len(result)+1,
                    'Material_transformation_id': mtp['ID'],
                    'Type': cond[0],
                    'Quantity': cond[1],
                    'Condition': cond_id.replace('_', ' '),
                    'Unit': cond[2]
                })

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
    for input in itemlits:
        chem = input['Chemical']
        if not chem in chem_list:
            chem_list.append(chem)
            result.append({'ID': len(result)+1,
                'Chemical': chem
            })

    return result