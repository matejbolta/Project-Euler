'''
Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, tn = n * (n + 1) / 2;
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
'''
import os
os.getcwd() #UVP_2020
os.chdir('project_euler')
os.chdir('txt_files')

slovar = {} #iz crke v stevilko
abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i, crka in enumerate(abeceda):
    slovar[crka] = i + 1 #slovar narejen.

tri = set() #mnozica trikotnih
st = 0
for i in range(1, 100): #max(tri) = 4950
    st += i
    tri.add(st)

def beseda2stevilo(niz):
    '''uporablja slovar'''
    st = 0
    for znak in niz:
        st += slovar[znak]
    return st

with open('p042_words.txt', 'r', encoding='utf-8') as besede:
    sez = besede.read().strip().split(',')
    #beseda v sez = element[1:-1]

ugodne = []
for beseda in sez:
    beseda = beseda[1:-1]
    stevilo = beseda2stevilo(beseda)
    if stevilo in tri:
        ugodne.append(beseda)
#len(ugodne)
#162