import shutil
import os
from conf.config import parser

def clean_directory(dir):
    # Deleting an non-empty folder
    dir_path = rf"{dir}"
    shutil.rmtree(dir_path, ignore_errors=True)
    os.mkdir(dir)

def get_file_directory_name(iri):
    doi = iri.split("/")[-1]
    filename = parser.get('files', 'output_name')+"_"+doi+"."+parser.get('files', 'extension')
    return parser.get('files', 'output_directory')+"/"+filename