from fileinput import filename
import os
from conf.config import parser
import requests
import csv
from colorama import Fore, Style
import uuid

output_directory = parser.get('files', 'output_directory')
page_url = parser.get('files', 'webpage')
os.chdir(os.path.dirname(__file__))
file_id_map = []

# Check whether the specified path exists or not
if not os.path.exists(output_directory):
  # Create a new directory because it does not exist 
  os.makedirs(output_directory)

print("Start downloading from Artleafs...")
with open(parser.get('files', 'data'), encoding = 'cp850') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filename = row['filename']
        doi = row['DOI']
        url = page_url+filename
        response = requests.get(url)
        new_filename = f"{uuid.uuid4()}.pdf"
        dir = rf"{output_directory}/{new_filename}"
        try:
            with open(dir, 'wb') as f:
                f.write(response.content)
                file_id_map.append({'DOI': row['DOI'], 'file': new_filename})
        except Exception:
            print(f"\tError downloading {Fore.RED}{doi}{Style.RESET_ALL}: {filename}")

    fieldnames = list(file_id_map[0].keys())
    with open(parser.get('files', 'map_file'), 'w', errors='surrogatepass', encoding="utf8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(file_id_map)
        
print(f"Download finished. Check {Fore.BLUE}{output_directory}{Style.RESET_ALL}")

