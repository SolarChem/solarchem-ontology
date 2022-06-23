from db_connect import cursor
from utils import *
import re
import pycountry

def prepare_articles():
    query = "SELECT * FROM paper_references"
    cursor.execute(query)

    result = cursor.fetchall()
    for i in range(len(result)):
        row = result[i]
        row['Title'] = dequote(row['Title'])
        row['Abstract'] = dequote(row['Abstract'])
        row['Authors'] = dequote(row['Authors'])
        row['Country'] = dequote(row['Country'])
        row['Country_name'] = dequote(row['Country_name'])
        result[i] = row

    return result

def prepare_authors(articles):
    result = []
    for article in articles:
        article_id = article['ID']
        author_names = re.split(",\s*", article['Authors'])
        countries = re.split(",\s*", article['Country'])
        country_names = re.split(",\s*", article['Country_name'])
        for i in range(len(author_names)):
            author_id = len(result)+1
            c = None 
            cname = None

            if len(countries) > i:
                country = pycountry.countries.get(alpha_2=countries[i])
                if country:
                    c = country.alpha_2
                    cname = country.name
            
            author = {'ID': author_id,
                'paperID': article_id,
                'name': author_names[i],
                'country': c,
                'country_name': cname
                }
            
            result.append(author)

    return result