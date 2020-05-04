'''
Square digit chains
A number chain is created by continuously adding the square of
the digits in a number to form a new number until it has been
seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become
stuck in an endless loop. What is most amazing is that
EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
def naslednji(n):
    return sum([int(i)**2 for i in str(n)]) #izpeljano

import itertools

stevec = 0
for testna in range(1, 10 ** 7):
    if not testna % 10 ** 5: #napredek
        print(f'{testna // 10 ** 5}%, stevec = {stevec}')
    for _ in itertools.count():
        if testna == 1:
            break
        elif testna == 89:
            stevec += 1
            break
        testna = naslednji(testna)
print(f'konec:{stevec}')
#konec:8581146