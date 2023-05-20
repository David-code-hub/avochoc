#python3 -m pip install rapidfuzz
#python3 -m pip install python-Levenshtein 
from rapidfuzz import fuzz,process
import csv
import time

listofphrases = []
with open('../files/researchlv2num1.csv', 'r') as searchdb:
    searchdb_ = csv.reader(searchdb,delimiter='\t')
    counter = 0
    for s in searchdb_:
        counter += 1
        if s:
            listofphrases.append(s[0])
    
def fuzzySearch():
    search_term = input('What are you looking for? ')
    st = time.time()
    print('searching for similar words...')
    print('related words :',process.extractOne(search_term,listofphrases)[0])
    print(f'1 result({(time.time() - st)} seconds)')
    more = input('Search for more related words?(yes or no) ')
    if more == 'yes':
        st = time.time()
        related_words = process.extract(search_term,listofphrases,limit=3)
        first,second,third = related_words[0][0],related_words[1][0],related_words[2][0]
        print('################################################')
        print('################################################')
        print(f"other related words : '{first}', '{second}', '{third}'")
        print(f'3 results({(time.time() - st)} seconds)')
    return

fuzzySearch()
