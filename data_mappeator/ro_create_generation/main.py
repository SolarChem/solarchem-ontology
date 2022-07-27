from conf.config import parser
import csv
import os
from utils import create_ro_crate
from FileMap import FileMap
from alive_progress import alive_bar

os.chdir(os.path.dirname(__file__))

map_file = {}

# Adding data to the maps
with open(parser.get('files', 'map_file_pdf')) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        doi = row['DOI'].strip() # los strip son debidos a un fallo en la extracción de datos
                                 # se corregida en versiones futuras
        map_file[doi] = FileMap(doi, row['file'])

with open(parser.get('files', 'map_file_rdf')) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        doi = row['DOI'].strip()
        filemap = map_file[doi]
        filemap.rdf = row['file']

print("Creating the RO-Crates...")
with alive_bar(len(map_file)) as bar:
    for doi in map_file:
        # Creating the RO-Crate
        filemap = map_file[doi]
        create_ro_crate(doi, filemap.pdf, filemap.rdf)
        bar()



