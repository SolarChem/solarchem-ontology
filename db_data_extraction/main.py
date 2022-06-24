from data_inicializator import *
from utils import *

#Preparamos la información
articles = prepare_articles()
authors = prepare_authors(articles)
material_tranformations = prepare_material_transformations()
inputs = prepare_inputs(material_tranformations)


#Generamos los csv
createCsv(articles, 'paper_references.csv')
createCsv(authors, 'authors.csv')
createCsv(material_tranformations, 'material_transformations.csv')
# TODO: createCsv(inputs, 'inputs.csv')