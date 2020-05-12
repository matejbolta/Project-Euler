'''
Spiral primes 
Problem 58

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
'''
import itertools

#diagonalnih elementov:
# 1-1   3-5   5-9   7-13
# stranica n, diagonalnih pa je ((n-1)/2)*4 + 1

#ko gremo na n=3 se pomaknemo 4x za 2         (da smo na diagonali)
#            n=5              4x za 4
#            n=7                    6
#            n=2k+1                 2k

#iscemo, kdaj je ratio = prime / diagonalne  <  0.1

def prime(n):
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

kandidat = 1
prastevila = 0
for k in itertools.count(1):

    n = 2 * k + 1  #dolzina stranice

    #if not n % 1001:
    #    print(n) #napredek

    for _ in range(4):
        kandidat += 2 * k
        if prime(kandidat):
            prastevila += 1
    
    if prastevila / (((n - 1) / 2) * 4 + 1) < 0.1:
        print(n) #26241
        break
