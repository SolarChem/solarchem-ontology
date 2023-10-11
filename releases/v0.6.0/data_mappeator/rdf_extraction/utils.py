import shutil
import os
from conf.config import parser
import urllib.parse

def clean_directory(dir):
    # Deleting an non-empty folder
    dir_path = rf"{dir}"
    shutil.rmtree(dir_path, ignore_errors=True)
    os.mkdir(dir)

def get_file_directory_name(doi):
    filename = get_filename(doi)
    return parser.get('files', 'output_directory')+"/"+filename

def get_filename(doi):
    # the filename will be a URL parsed DOI to be the same as the individual IRI
    parsed_doi = urllib.parse.quote(doi, safe='')
    return parsed_doi+"."+parser.get('files', 'extension')