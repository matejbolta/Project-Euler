'''
Truncatable primes

The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def prastevilo(n):
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

def truncatable(n):
    if not prastevilo(n):
        return False
    shranjen_n = n
    while n > 0: #režemo z desne
        if not prastevilo(n):
            return False
        n //= 10
    while shranjen_n > 0: #režemo z leve
        if not prastevilo(shranjen_n):
            return False
        shranjen_n = int(str((int(str(shranjen_n)[::-1]) // 10))[::-1]) # n = n brez prve števke
    return True

kandidat = 10 #za <10 ne upoštevamo
sez = []
while len(sez) != 11:
    if truncatable(kandidat):
        print(kandidat)
        sez.append(kandidat)
    kandidat += 1

print(sum(sez))

'''
23
37 
53 
73 
313
317
373
797
3137
3797
739397
sum = 748317
'''
