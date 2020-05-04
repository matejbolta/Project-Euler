'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be
written as the sum of a prime and twice a square?
'''
def prime(n): #iz vaj
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

prastevila = [] #seznam prastevil do miljon
for i in range(2, 5000): #po dobljeni rešitvi sem zmanjšal na 5000
    if prime(i):
        prastevila.append(i)
print('prastevila narejena')

def x_prastevilo_plus_dvakratnik_kvadrata(n):
    for prastevilo in prastevila:
        if n - prastevilo < 0:
            return False
        vmesen = ((n - prastevilo) / 2)**(1/2) #ALI DRŽI: vmesen = x, kjer je x naravno število?
        if vmesen.is_integer():
            return True #našli smo prave številke, da je n = prime + 2 * kvadrat
    
x = 9
while True:
    if not x % 100:
        print(f'napredek:{x}')
    if prime(x):
        x += 2
        continue
    if x_prastevilo_plus_dvakratnik_kvadrata(x): #ko je to False, končamo
        x += 2
        continue
    print(f'našli smo to število:{x}')
    break


'''
prastevila narejena
našli smo to število:5777
>>> 
'''