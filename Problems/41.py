'''
Pandigital prime

We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def pandigital(n):
    ohranim = n
    if len(str(n)) > 9:
        return False
    sez = []
    while n != 0:
        sez.append(n % 10)
        n //= 10
    return sorted(sez) == [i for i in range(1, len(str(ohranim)) + 1)]

def prime(n): #uradna resitev iz tomo vaj
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

#ze resitev ampak dolgo dela
#largest = max({i for i in range(10**9) if pandigital(i) and prime(i)})

# vseh pandigital stevil je toliko:
# >>> from math import factorial
# >>> vsota = 0    
# >>> for i in range(1, 10):
# ...     vsota += factorial(i)
# >>> vsota
# 409 113
#procent prastevil do n je 1/ln(n)
#torej 1/log(10**9) * 10**9 = 48 254 942

#pandigital stevil je manj kot prime.
#naredil bom mnozico pandigital do 10**9, pol se bom pa vozu cez to mnozico

pan = set()
for i in range(1, 10**9):
    if not i % (5 * 10**6): #vsake 5 milijonov sprintamo napredek. gremo do miljarde
        print(i)
    if pandigital(i):
        pan.add(i)
    if i == 10**9 - 1:
        print('pan narejena!')
        print(f'stevilo pandigital stevil:{len(pan)}')

#mnozico pan dela priblizno 1 uro, naprej pa v 1 sekundi

panpri = set()
for i, st in enumerate(pan):
    if prime(st):
        panpri.add(st)
print(f'stevilo ugodnih stevil:{len(panpri)}')
najvecji = max(panpri)
print(f'tole je najvecja stevilka od ugodnih:{najvecji}')

#pan narejena!
#stevilo pandigital stevil:409113            (pravilno sem jih ocenil!!)
#stevilo ugodnih stevil:538
#tole je najvecja stevilka od ugodnih: 7652413