from conf.config import parser
import urllib.parse
from rocrate.rocrate import ROCrate

def create_ro_crate(doi, pdf_filename, rdf_filename):
    crate = ROCrate()
    output_folder = parser.get('files', 'output_directory')
    parsed_doi = urllib.parse.quote(doi, safe='')

    pdf_dir = parser.get('files', 'pdf_directory')+pdf_filename
    rdf_dir = parser.get('files', 'rdf_directory')+rdf_filename
    paper = crate.add_file(pdf_dir, properties={
        "name": "manuscript",
        "encodingFormat": "application/pdf"
    })
    rdf = crate.add_file(rdf_dir, properties={
        "name": "linked data",
        "encodingFormat": "text/turtle"
    })

    crate.write(f"{output_folder}dir/{parsed_doi}")
    crate.write_zip(f"{output_folder}zip/{parsed_doi}.zip")

def dequote(s: str):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s and s.startswith(("'", '"')) and s[0] == s[-1]):
        return s[1:-1]
    return s