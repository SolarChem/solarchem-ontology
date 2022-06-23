import csv
import unicodecsv
import os
import re
import json

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s.startswith(("'", '"')) and s[0] == s[-1]):
        return s[1:-1]
    return s

def createCsv(data, file_name):
    file_name = os.path.join(os.path.dirname(__file__), 'data', file_name)
    fieldnames = list(data[0].keys())
    with open(file_name, 'w', errors='surrogatepass') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)

def unicodeToPlain(s):
    unicodes = re.findall(r'\\u[\w]{4}', s)
    for ucode in unicodes:
        c = dequote(json.dumps(json.loads(r'"%s"' % ucode), ensure_ascii=False))
        s = s.replace(ucode, c)
    return s

def cleanText(s):
    s = dequote(s)
    s = unicodeToPlain(s)
    return s
