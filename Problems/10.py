'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import sys
sys.setrecursionlimit(2000000)

def je_deljivo_s_katerim_od(n, seznam):
    '''Vrne 'True' natanko tedaj, ko je število 'n' deljivo
    z vsaj kakšnim številom iz seznama števil 'seznam'. '''
    if len(seznam) == 0:
        return False
    elif n % seznam[0] == 0:
        return True
    else:
        return je_deljivo_s_katerim_od(n, seznam[1:])

def prastevila_do(n):
    '''Vrne seznam vseh praštevil, ki so
    manjša ali enaka podanemu številu.'''
    if n <= 1:
        return []
    elif not je_deljivo_s_katerim_od(n, prastevila_do(n - 1)):
        return prastevila_do(n - 1) + [n]
    else:
        return prastevila_do(n - 1)

x = sum(prastevila_do(2000000))

print(x)
