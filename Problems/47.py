'''The first two consecutive numbers to have two
distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have
three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers
to have four distinct prime factors each. What is
the first of these numbers?'''

#slovar za memoizacijo
#slovar = {} #slovar['n'] = set(prafaktorji od n)
def prafaktorji(n):
    '''vrne mnozico prafaktorjev'''
    #if str(n) in slovar:
    #    return slovar[str(n)]
    if n == 1:
        return set()
    mno = set()
    i = 2
    while n % i: #i se poveča, dokler ne deli n
        i += 1
    mno.add(i)
    #slovar[str(n)] = slovar.get(str(n), set()).union({i})
    return mno.union(prafaktorji(n // i))

import itertools
for i in itertools.count(2):
    if not i % 10000:
        print(i) #napredek
    if 4 == len(prafaktorji(i)) == len(prafaktorji(i+1)) == len(prafaktorji(i+2)) == len(prafaktorji(i+3)):
        print(f'prvo število od štirih: {i}')
        break

'''
10000
20000
30000
40000
50000
60000
70000
80000
90000
100000
110000
120000
130000
prvo število od štirih: 134043
'''