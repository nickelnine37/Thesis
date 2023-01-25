import bibtexparser

"""
Quick python script to format the bib file
"""



with open('Bibliography.bib', 'r+') as f:
    bib_database = bibtexparser.load(f)


for item in bib_database.entries:

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
