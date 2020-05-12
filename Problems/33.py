sez = []
for desetica1 in range(1, 10):
    for enica1 in range(1, 10):
        for desetica2 in range(1, 10):
            for enica2 in range(2, 10):
                x = (10*desetica1 + enica1) / (10*desetica2 + enica2)
                if x < 1:
                    if x == desetica1 / enica2:
                        #if not(desetica1 == enica1 and desetica2 == enica2):#odstanjujem trivialne
                        if enica1 == desetica2:
                            print(desetica1, enica1, desetica2, enica2)
                            sez.append('_')
                    if x == desetica1 / desetica2:
                        if enica1 == enica2:
                            print(desetica1, enica1, desetica2, enica2)
                            sez.append('_')
                    if x == enica1 / enica2:
                        if desetica1 == desetica2:
                            print(desetica1, enica1, desetica2, enica2)
                            sez.append('_')
                    if x == enica1 / desetica2:
                        if desetica1 == enica2:
                            print(desetica1, enica1, desetica2, enica2)
                            sez.append('_')

print(len(sez)) #teh števil je 
'''
1 6 6 4   1/4
1 9 9 5   1/5
2 6 6 5   2/5
4 9 9 8   1/2
4
'''

stevec = 1*1*2*1     #2
imenovalec = 4*5*5*2     #200
#produkt = 2/200 = 1/100
#resitev 100
