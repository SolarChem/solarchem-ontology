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
    parsed_doi = urllib.parse.quote(doi, safe='')
    filename = parsed_doi+"."+parser.get('files', 'extension')
    return parser.get('files', 'output_directory')+"/"+filename