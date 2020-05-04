#kombinatorika = lajf

from math import factorial as fac

#40 nad 20:  40! / (20! * 20!)

a = fac(40) / (fac(20) * fac(20))

print(int(a))