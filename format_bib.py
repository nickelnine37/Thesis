import os
import bibtexparser

"""
Quick python script to format the bib file
"""



with open('Bibliography.bib', 'r+') as f:
    bib_database = bibtexparser.load(f)


skipitems = ['EPA2023', 'FRED2023', 'ONS2019', 'Bradbury2018', 'Wang2022b', 'Wang2022c']

for item in bib_database.entries:

    if item['ID'] in skipitems:
        continue

    item['ID'] = item['author'].split(',')[0].strip() + item['year'] 

    remove_keys = ['abstract', 'keywords', 'file', 'note']

    for key in remove_keys:

        if key in item:
            del item[key]

    if 'doi' in item:

        item['url'] = f'https://doi.org/{item["doi"]}'

    else:

        print(f'Warning: no doi found for entry {item["ID"]}')


with open('Bibliography.bib', 'w') as f:
    bibtexparser.dump(bib_database, f)


text = ''

for fname in os.listdir('Chapters'):

    with open(f'Chapters/{fname}') as f:

        text += f.read()


for item in bib_database.entries:

    if item['ID'] not in text:

        print(f'Warning: {item["ID"]} not cited')