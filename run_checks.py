import os
import re

def check_abbreviations():

    content_tex = ''

    for fname in os.listdir('Chapters'):

        with open(f'Chapters/{fname}') as f:

            content_tex += f.read()

    content_abs = set([s.strip() for s in re.findall(r' [A-Z]{3} ', content_tex)])

    with open('Front & Back Matter/abbreviations.tex') as f:

        ab_tex = f.read()

    listed_abs = set([s.strip() for s in re.findall(r'[A-Z]{3} ', ab_tex)])

    for ab in content_abs:

        if ab not in listed_abs:
            print(f'Warning: abbreviation {ab} not listed in abbreviations.tex')


if __name__ == '__main__':

    check_abbreviations()