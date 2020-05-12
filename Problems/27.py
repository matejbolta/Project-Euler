'''
(n * n) + (a * n) + b
'''

import itertools

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

mnozica_prastevil = set()
for stevilo in range(1, 999 * 1000):
    if je_prastevilo(stevilo):
        mnozica_prastevil.add(stevilo)
#zdaj imam dovolj veliko mnozico prastevil do 10**6

#ker se maximum pritozi ce mu damo dva argumenta v funkcijo za key, ga bom zapakiral v nabor
#nabor = (a, b)
def stevilo_prastevil_ce_vstavimo(nabor):
    '''vrne stevilo zaporednih prastevil, ce v formulo vstavimo a in b'''
    a, b = nabor
    for i in itertools.count(0, 1):
        x = (i ** 2) + (a * i) + b
        if x not in mnozica_prastevil:
            return i

resitev = max(((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)), key=stevilo_prastevil_ce_vstavimo)
#v resitev sta zdej a in b, ki sproducirata največje število praštevil

zmnozek = resitev[0] * resitev[1]

print(zmnozek)

#deluje!

#resitev = (-61, 971)
#zmnozek = -59231
#mimogrede, sproducirata 71 praštevil.