def memoiziraj(funkcija):
    rezultati = {}
    def mem_funkcija(x):
        if x not in rezultati:
            rezultati[x] = funkcija(x)
        return rezultati[x]
    return mem_funkcija

@memoiziraj
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

'''By considering the terms in the Fibonacci sequence whose values do 
not exceed four million, find the sum of the even-valued terms.'''

sode = 0
n = 1
while fib(n) <= 4000000:
    if fib(n) % 2 == 0:
        sode += fib(n)
    n += 1

#sode = 4613732