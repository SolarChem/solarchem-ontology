from conf.config import parser
import csv
import os
from utils import create_ro_crate

os.chdir(os.path.dirname(__file__))

map_file = {}

# Adding data to map
with open(parser.get('files', 'map_file')) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        map_file[row['DOI']] = row['file']


# Linking the map with the data
with open(parser.get('files', 'input_data'), encoding = 'cp850') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        doi = row['DOI']
        pdf_filename = map_file[doi]
        create_ro_crate(doi, pdf_filename)
