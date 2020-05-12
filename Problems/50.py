'''
Consecutive prime sum
   
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def prime(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else: #vsa liha ostanejo
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

prast = [] #seznam prastevil do miljon (cca 78 500 jih je)
for i in range(2, 10 ** 6):
    if prime(i):
        prast.append(i)
print('prast narejena')

najdaljsa, resitev = 0, 0
for i, prastevilo in enumerate(prast):
    if not i % 10000: #za napredek
        print(i)
    vsota, zaporednih = prastevilo, 1
    for j, drugo_prastevilo in enumerate(prast[i + 1:]):
        vsota += drugo_prastevilo
        zaporednih += 1

        if vsota > 10 ** 6: #gremo na naslednjo verigo, naslednji i
            break

        if prime(vsota) and zaporednih > najdaljsa:
            resitev, najdaljsa = vsota, zaporednih

print(f'najvecja vsota:{resitev}, stevilo clenov  v vsoti:{najdaljsa}')

'''
prast narejena
0
10000
20000
30000
40000
50000
60000
70000
najvecja vsota:997651, stevilo clenov  v vsoti:543
'''
