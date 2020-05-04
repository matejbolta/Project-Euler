'''
Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def je_prastevilo(n):
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

def zamakni(x):
    '''da prvo števko na konec'''
    niz = str(x)
    zlepek = niz[1:] + niz[0]
    return zlepek


def je_krozno_prastevilo(n):
    '''true, če je, false, če ni'''
    if not je_prastevilo(n):
        return False
    x = zamakni(n) #x je string zdej
    while int(x) != n:
        if not je_prastevilo(int(x)):
            return False
        else:
            x = zamakni(x)
    return True

def koliko_je_kroznih_prastevil_manjsih_od(n):
    rezultat = 0
    for x in range(n):
        if je_krozno_prastevilo(x):
            rezultat += 1
    return rezultat

print(koliko_je_kroznih_prastevil_manjsih_od(10**6))

#100 13
#1000 25
#10 000 33
#100 000 43
#1 000 000 55 JA!