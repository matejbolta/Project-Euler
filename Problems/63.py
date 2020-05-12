'''
Powerful digit counts
The 5-digit number, 16807=7**5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an n-th power?
'''

def taka_stevila_do(x=10 ** 4):
    stevec = 0
    for i in range(1, x):
        osnova = 1
        while osnova ** len(str(i)) <= i:
            if osnova ** len(str(i)) == i:
                stevec += 1
                break
            osnova += 1
    return stevec
#do 10**4 24
#     **5 27
#     **6 30
#     **7 32
#dela zelo dolgo 

#------------

#če gledamo osnova ** potenca, mora biti očitno 0 < osnova < 10
#lahko omejimo tudi potenco?

for potenca in range(5):  #za osnova = 5 je ok že, če gre potenca do vkljucno 4
    #print(len(str(5 ** potenca)))
    pass
#najbol robne primere bomo pa pokrili, če preverim najvecjo osnovo = 9
for potenca in range(23):
    #print(len(str(9 ** potenca)))
    pass
#z povecevanjem ugotovimo, da ko pridemo do 22, je najvecja dolzina 21,
# kar je premalo, nato pa se razlika samo se povecuje

stevec = 0
for osnova in range(1, 10):
    for potenca in range(1, 23):
        if len(str(osnova**potenca)) == potenca:
            stevec += 1
print(stevec) #49
