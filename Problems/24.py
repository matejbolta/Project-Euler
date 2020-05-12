'''
A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations

nabor = tuple(range(10))
sez_urejene_permutacije = list(permutations(nabor))
x = sez_urejene_permutacije[999999]

#print(x)

#dajmo še v številko

x = list(x)
for i, st in enumerate(x):
    x[i] = f'{st}'
x = ''.join(x)

#...
print(x)
