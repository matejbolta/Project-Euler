from math import factorial as fac

def binomial(x, y):
    return (fac(x) // fac(y)) // fac(x - y)

stevec = 0
for n in range(23, 101):
    for r in range(n):
        if binomial(n, r) > 10 ** 6:
            stevec += 1

#stevec = 4075