from conf.config import parser
import urllib.parse
from rocrate.rocrate import ROCrate

def create_ro_crate(doi, pdf_filename):
    crate = ROCrate()
    output_folder = parser.get('files', 'output_directory')
    parsed_doi = urllib.parse.quote(doi, safe='')

    pdf_dir = parser.get('files', 'pdf_directory')+pdf_filename
    rdf_dir = parser.get('files', 'rdf_directory')+parsed_doi+".ttl"
    print(rdf_dir)
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