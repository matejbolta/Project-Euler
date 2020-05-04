'''
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated
product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can
be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?
'''

baza = ['1','2','3','4','5','6','7','8','9']

def f(x):
    '''sez stevk'''
    return list(str(x))

def g(x):
    '''iz seznama v število'''
    return int(''.join(x))

# n * m = pan, za vse n skupaj
resitev = 0
for n in range(2, 10): #najvecji n je lahko 9
    for m in range(1, 10 ** (9 // n)):
        #za n = 1 je lahko m dolg 9
        #za n = 2 je lahok m dolg 4
        #za n = 3 je lahko m dolg 3
        #za n = 4 je lahko m dolg 2
        #za n = 5,6,7,8,9 je lahko m dolg 1
        sez = []
        for n in range(1, n + 1):
            sez += f(m * n)
        if sorted(sez) == baza and g(sez) > resitev:
            resitev = g(sez)
print(f'tole je rešitev: {resitev}')

'''
tole je rešitev: 932718654
'''