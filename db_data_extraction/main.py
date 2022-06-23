from data_inicializator import *
from utils import *

#Preparamos la información
articles = prepare_articles()
authors = prepare_authors(articles)


#Generamos los csv
createCsv(articles, 'paper_references.csv')
createCsv(authors, 'authors.csv')