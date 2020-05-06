2969
6299
9629

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

for x in range(1000, 10000-2*3330):
    if sorted(list(str(x))) == sorted(list(str(x + 3330))) == sorted(list(str(x + 2*3330))):
        if prime(x):
            if prime(x + 3330):
                if prime(x + 2*3330):
                    print(f'{x}{x+3330}{x+2*3330}')

'''
148748178147
296962999629
'''