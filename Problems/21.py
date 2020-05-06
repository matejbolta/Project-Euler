'''
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors
of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def vsota_deliteljev(n):
    delitelji = []
    polovic = (n // 2) + 1
    for i in range(1, polovic):
        if n % i == 0:
            delitelji.append(i)
    return sum(delitelji)

def sta_amicable_par(a, b): #ne rabim uresnici
    return (a != b) and (vsota_deliteljev(a), vsota_deliteljev(b)) == (b, a)

def je_amicable(a):  #to pa rabim
    b = vsota_deliteljev(a)
    return (a != b) and (vsota_deliteljev(b) == a)

#koliko je vsota vseh amicable stevil 1 - 9 999?

#from itertools import count

rtr = 0
for i in range(1, 10000):
    if je_amicable(i):
        rtr += i

print(rtr)