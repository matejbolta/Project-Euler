'''
Reciprocal cycles

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
'''

seznam = []
for i in range(2, 1000):
    seznam.append(1 / i)


def dolzina_periode(n):
    while True: #prestavi prvo nenicelno decimalko na prvo mesto
        if int(10 * n) != 0:
            break
        else:
            n *= 10
    
    sez = list(str(n))
    del sez[0]
    del sez[0]

    for i, element in enumerate(sez):
        sez[i] = int(element)

    #sedaj imamo seznam posameznih decimalk od prve neničelne do zadnje

    preverjamo = []
    for i, element in enumerate(sez):
        if element not in preverjamo:
            preverjamo.append(element)
            if i == len(sez) - 1:  #za tiste ki nimajo periode
                return 0
        else:
            indeks = preverjamo.index(element)
            dolzina = len(preverjamo[indeks:])
            break

    return dolzina
    

resitev = max(seznam, key=dolzina_periode)

print(resitev)
#sprinta 0.012345679012345678, kar je pričakovano

from fractions import Fraction
print(str(Fraction(resitev)))
#zaradi pythonovega zaokrozevanja vrne priblizek in ne 1 / 81
#online kalkulator je razrešil zadevo




#rezultat 81 je napacen :(
    #mission abort
#---------------------------------------------------------

#zapis x na i decimalk
#f'{x:.if}'