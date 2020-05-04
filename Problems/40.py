'''
An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910 1 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def razbij_na_stevke(n):
    '''vrne seznam''' #izpeljano hehe
    return [i for i in str(n)]
    
#note:tole bi lahko hitro napisal na grdo, ampak bom probal splošno za katerikoli n. pri nas je n = 6
def zmnozek_10ih_potenc_od_x_do_potence(n):
    #naredimo seznam stevk
    sez = [0]
    i = 1
    while len(sez) < 10 ** n + 1:
        sez.extend(razbij_na_stevke(i))
        i += 1
    #dovolj dolg seznam imamo
    zmnozek = 1
    for k in range(n + 1):
        zmnozek *= int(sez[10 ** k])
    return zmnozek

#>>> zmnozek_10ih_potenc_od_x_do_potence(6)
#210