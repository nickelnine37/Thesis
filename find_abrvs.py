import re
import os

text = ''

for fname in os.listdir('Chapters'):

    with open(f'Chapters/{fname}') as f:

        text += f.read()

matches = set(re.findall(r'[A-Z]{3}', text))

for m in matches:
    ind = text.index(m)
    print(m, text[ind - 10:ind + 10])

