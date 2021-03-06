'''
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import permutations

#baza = [f'{i}' for i in range(10)]
#def pandigital(n): #deluje za pandigital 0-9
#    return sorted(list(str(n))) == baza

def f(x):
    '''nabor v niz'''
    niz = ''
    for z in x:
        niz += str(z)
    return niz

vsota = 0
for i in permutations(list(range(10))):
    if int(f(i)[1:4]) % 2 or int(f(i)[2:5]) % 3 or int(f(i)[3:6]) % 5 or int(f(i)[4:7]) % 7 or int(f(i)[5:8]) % 11 or int(f(i)[6:9]) % 13 or int(f(i)[7:10]) % 17:
        continue
    vsota += int(f(i))
    print(f'---{int(f(i))}')
print(f'vsota: {vsota}')

'''
---1406357289
---1430952867
---1460357289
---4106357289
---4130952867
---4160357289
vsota: 16695334890
'''
