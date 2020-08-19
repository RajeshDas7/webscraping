import requests
import csv

with open('ENTITIES_WIKIDATA_1.csv','r') as inp:
    for row in csv.reader(inp):
        print(row[4])
        try:

            url = 'https://www.wikidata.org/wiki/Special:EntityData/'  +  str(row[4])  +  '.rdf'
            r = requests.get(url, allow_redirects=True)
            open(str(row[4])+'.rdf', 'wb').write(r.content)
        except Exception as e:
            print(e)


print("done")