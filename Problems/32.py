'''
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

baza = ['1','2','3','4','5','6','7','8','9']

def f(x):
    '''sez stevk'''
    ss = []
    for j in str(x):
        ss.append(j)
    return ss

def seznam(a, b, x):
    '''sez stevk od a,b,x'''
    x = f(a) + f(b) + f(x)
    return sorted(x)

##  a * b == x
#vsota = set()
#for a in range

vsota = set()
sez = []
for a in range(1, 10**4):
    if not a % 100:
        print(f'a : {a}') #napredek
    for b in range(1, 10**4):
        if seznam(a, b, a*b) == baza:
            print(f'----------------{a} * {b} = {a*b}--------------')
            vsota.add(a*b)
            sez.append(a*b)

print(f'dolzina mnozice: {len(vsota)}, vsota mnozica: {sum(vsota)}\nza primerjavo, dolzina seznama: {len(sez)}')

'''
dolzina mnozice: 7, vsota mnozica: 45228
za primerjavo, dolzina seznama: 18
'''
