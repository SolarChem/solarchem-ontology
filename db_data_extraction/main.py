from data_inicializator import *
from utils import *

#Preparamos la información
articles = prepare_articles()
journals = prepare_journals(articles)
authors = prepare_authors(articles)
material_tranformations = prepare_material_transformations()
inputs = prepare_inputs(material_tranformations)
conditons = prepare_conditions(material_tranformations)
outputs = prepare_outputs(material_tranformations)
chemicals = prepare_chemicals([*inputs, *outputs])


#Generamos los csv
createCsv(articles, 'paper_references.csv')
createCsv(journals, 'journals.csv')
createCsv(authors, 'authors.csv')
createCsv(material_tranformations, 'material_transformations.csv')
createCsv(inputs, 'inputs.csv')
createCsv(conditons, 'conditons.csv')
createCsv(outputs, 'outputs.csv')
createCsv(chemicals, 'chemicals.csv')