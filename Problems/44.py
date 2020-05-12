'''
Pentagonal numbers are generated by the formula,
Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk,
for which their sum and difference are pentagonal
and D = |Pk − Pj| is minimised; what is the value of D?
'''

#zdaj pa že poznam generatorje
#zaporedni pentagonal števili sta si čedalje bolj narazen
def generator_pentagonalnih():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

gen1 = generator_pentagonalnih()
baza = set([next(gen1) for _ in range(10**4)])
#upam da dovolj velika baza

gen2 = generator_pentagonalnih()

x = 10**1000
for z, _ in enumerate(baza):
    if not z % 1000:
        print(f'napredek: {z}') #napredek
    pent = next(gen2)
    for bazni in baza:
        if pent + bazni in baza and pent - bazni in baza:
            x = min(x, abs(pent - bazni))
            print(f'---------nov najmanjsi: {x}')

'''
napredek: 0
napredek: 1000
napredek: 2000
---------nov najmanjsi: 5482660
napredek: 3000
napredek: 4000
napredek: 5000
napredek: 6000
napredek: 7000
napredek: 8000
napredek: 9000
'''
