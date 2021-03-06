'''
Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
36 - 9
45 - 6
55 - 4
66 - 8
78 - 8
91 - 4
105 - 8
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
def stevilo_deliteljev(n): #učinkovita
    x = 0
    polovic = (n // 2) + 1
    for i in range(1, polovic):
        if n % i == 0:
            x += 1
    return x + 1

import itertools                    #za neksončen range

trikotna = 0
for i in itertools.count(1):         #neskončen range po 1
    trikotna += i
    print(i)
    #print(stevilo_deliteljev(trikotna))
    if stevilo_deliteljev(trikotna) > 500:
        print(trikotna)     #tekel bi v neskončno, ampak sprinta prvo pravo stevilko in nato breaka
        break

#start ob 21:58
#22:01 na 2370
#22:15 na 4100

#22:29 na 5000
#22:52 na 6000
#23:34 na 7200   23:45 na 7500
#00:12 na 8100   00:37 na 8500
#01:09 na 9000   01:49 na 9550
#grem spat
#ob 8:25 je ze koncal
#zadnja sprintana stevilka je 12375
#sprintana trikotna je 76576500

#12375-to zaporedno trikotno stevilo je to. deluje.
