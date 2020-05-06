#iz vaj
def naslednji_clen(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

@memoiziraj
def dolzina_zaporedja(n):
    dolzina = 1
    while n != 1:
        dolzina += 1
        n = naslednji_clen(n)
    return dolzina

def memoiziraj(funkcija):
    rezultati = {}
    def mem_funkcija(x):
        if x not in rezultati:
            rezultati[x] = funkcija(x)
        return rezultati[x]
    return mem_funkcija



x = max(range(1, 1000000), key=dolzina_zaporedja)



print(x)