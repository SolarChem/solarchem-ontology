import csv
import os
import re
import json

def dequote(s: str):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s and s.startswith(("'", '"')) and s[0] == s[-1]):
        return s[1:-1]
    return s

def createCsv(data, file_name):
    file_name = os.path.join(os.path.dirname(__file__), 'data', file_name)
    fieldnames = list(data[0].keys())
    with open(file_name, 'w', errors='surrogatepass', encoding="utf8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)

def unicodeToPlain(s):
    unicodes = re.findall(r'\\u[\w]{4}', s)
    for ucode in unicodes:
        c = dequote(json.dumps(json.loads(r'"%s"' % ucode), ensure_ascii=False))
        s = s.replace(ucode, c)
    return s

def cleanText(s: str):
    s = dequote(s)
    s = unicodeToPlain(s)
    s = s.replace('\r', '').replace('\n', ' ') # remove the line breaks
    s = re.sub('\s+',' ',s)
    return s

def clean_empties(s):
    """
    Converts empty fields to None.
    An field is empty if its value is an empty string, -1 or N/A 
    """
    saux = s
    if isinstance(saux, str):
        saux = saux.lower()

    if saux == '' or saux == -1 or saux == 'n/a' or saux == '-1':
        return None
    return s

def clean_row(row):
    """
    Converts empty fields in a row to None.
    An field is empty if its value is an empty string, -1 or N/A 
    """
    for idx in row:
        row[idx] = clean_empties(row[idx])
        if isinstance(row[idx], str):
            row[idx] = cleanText(row[idx])
 
    return row

def check_if_all_none(list_of_elem):
    """ Check if all elements in list are None """
    result = True
    for elem in list_of_elem:
        if elem is not None:
            return False
    return result