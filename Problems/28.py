'''
Number spiral diagonals

Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the
numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in
a 1001 by 1001 spiral formed in the same way?
'''

#malo opazujem to spiralo, in so vedno na diagonali števke,
#ko se štirikrat premaknemo za korak naprej,
#nato pa korak povečamo za 2.
#korak je najprej 2

#dodajamo spodi ali zgoraj - spodaj na velikosti soda x soda
#                            zgoraj na velikosti liha x liha
#1001 x 1001:
#
# zacnemo z 1 x 1
# povecamo 500x spodaj in 500x zgoraj. dobimo 1001  x 1001
#-----------------------------------------------------
#KORAKI:
#štirikrat po 2 nam da 3x3 spiralo
#štirkrat po 4 nam da 5x5 spiralo
#štirikrat po 6 nam da 7x7 spiralo
#..        po n+2 nam da (n+2)x(n+2) spiralo

#začnimo s 1x1. nato jo povečamo za 1000 oziroma 500krat. dobimo 1001x1001 spiralo.
#prvič    4krat po 1*2 = 2    #spirala 3x3
#drugič   4krat po 2*2 = 4    #spirala 5x5
#tretjič  4krat po 3*2 = 6    #spirala 7x7
#  ...  
#499-ič  4krat po 499*2 = 998  #spirala 999x999
#zadnjič 4krat po 500*2 = 1000 #spirala 1001x1001
#_-----------------------------
#note:naša baza oziroma 1x1 spirala ima seštevek 1
#kaj seštevamo?
#1ki bomo 500krat prišteli štiri številke ki se razlikujejo za i, kjer
#je i korak prištevanja. ta korak gre od 2 do 1000 po skok 2

#zadnji ki smo ga prišteli v 1x1 je biu 1. nato pa:
# 3  5  7  9     +2
#13 17 21 25     +4
#31 37 43 49     +6
#57 65 73 81     +8
diagonala = 1
prištevam = 1
for korak in range(2, 1001, 2): #i je sedaj korak po koliko se premikamo. teh i-jev je 500.
    #i je korak
    for _ in range(4):
        #_ je število korakov. prvi drugi tretji četrti
        prištevam += korak
        diagonala += prištevam
#nakoncu izvajanja mora biti vsota v diagoala

print(diagonala) #669171001

#mam 3x3 matriko. korak je 4
#mam 1000x1000 matriko. korak za naprej je 1001, oziroma bi biu. ampak se ustavimo

