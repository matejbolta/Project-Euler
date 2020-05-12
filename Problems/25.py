'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

#import sys
#sys.setrecursionlimit(10 ** 6)
#dela tudi brez

def memoiziraj(funkcija):
    rezultati = {}
    def mem_funkcija(x):
        if x not in rezultati:
            rezultati[x] = funkcija(x)
        return rezultati[x]
    return mem_funkcija

@memoiziraj
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

from itertools import count
sez = count(1)  #neskoncen sez  [1, 2, 3, 4, 5, ...]
for i in sez:
    if len(str(fib(i))) == 1000:
        print(i)
        break
