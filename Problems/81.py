'''
Path sum: two ways
  
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

( 131  201  630  537  805 )
( 673  96   803  699  732 )
( 234  342  746  497  524 )
( 103  965  422  121  37  )
( 18   150  111  956  331 )

Find the minimal path sum from the top left to the bottom right by only moving right and down in
matrix.txt, a 31K text file containing an 80 by 80 matrix.
'''
#vseh moznih poti je 160 nad 80, torej 160! / 2*80!  =  3.3e165  :)  gremo torej efektivno
import os
os.getcwd() #Project-Euler
os.chdir('Project-Euler/txt_files')


#naredimo matriko
with open('p081_matrix.txt', 'r', encoding='utf-8') as in_file:
    matrika = []
    for vrstica in in_file:
        matrika.append(vrstica.strip().split(','))
#cleni so stringi namesto integerjev
for vrsta in matrika:
    for i, element in enumerate(vrsta):
        vrsta[i] = int(element)

#poskusimo podobno kot problema 18 in 67.
#sproti spreminjamo matriko tako da pristevamo najmanjso od opcij
def fun(matrix):
    for i in range(len(matrix)): #vrstice

        for j in range(len(matrix)): #gremo po eni vrstici

            if i > 0 and j > 0: #ne levo in ne zgoraj
                pristevek = min(matrix[i - 1][j], matrix[i][j - 1])

            elif i > 0: #cisto levo
                pristevek = matrix[i - 1][j]

            elif j > 0: #cisto zgoraj
                pristevek = matrix[i][j - 1]

            else: #v cisto prvem obhodu. matriki[0][0] pristejemo 0
                pristevek = 0

            matrix[i][j] += pristevek  #sproti spreminjamo matriko

    return matrix[len(matrix) - 1][len(matrix) - 1] #clen desno spodaj

print(fun(matrika))
#427337
#linux, pognano v terminalu ker mi taski ne delajo in jih ne morem vzpostavit :( 'no such file in directory'