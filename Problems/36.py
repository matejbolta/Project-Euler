'''
GOOGLE:
>>> 0b101111
47
>>> bin(173)
'0b10101101'
'''
def desetiskiVbinaren(desetiski):
    niz = bin(desetiski)
    return int(niz[2:])

def binarenVdesetiski(binaren):
    nizek = str(binaren)[::-1]
    resitev = 0
    potenca = 0
    for stevka in nizek:
        resitev += int(stevka) * (2 ** potenca)
        potenca += 1
    return resitev

def palindrom(st):
    return str(st) == str(st)[::-1]

vsota = 0
for i in range(1, 10**6):
    if palindrom(i) and palindrom(desetiskiVbinaren(i)):
        vsota += i
print(vsota)