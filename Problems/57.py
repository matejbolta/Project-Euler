'''
Square root convergents
'''

#opazim, da lahko namesto sqrt(2) obravnavam kar
# sqrt(2) - 1, in nakoncu stevcu se enkrat pristejem
# imenovalec ( v vlogi "ulomek + 1"), da dobim sqrt(2)

#prvih nekaj priblizkov je takih: (tisti, ki so v navodilih)
# 1 / 2
# 2 / 5
# 5 / 12
# 12 / 29

#opazim, da je naslednji stevec = prejsnji imenovalec
#opazim se, da je naslednji imenovalec = 2 * naslednji stevec + prejsnji stevec

rtr = 0 #steje pojavitve ki jih iscemo
stevec, imenovalec = 1, 2 #zacnemo z prvim priblizkom

for _ in range(999): #zacnemo z prvim priblizkom, ki itak ni v skladu s pogoji, nato zracunamo se naslednih 999

    stari_s, stari_i = stevec, imenovalec #shranimo stare
    stevec = stari_i
    imenovalec = 2 * stevec + stari_s

    if len(str(stevec + imenovalec)) > len(str(imenovalec)): #dodamo se +1
        rtr += 1

print(rtr) #153
#očitno so vsi ulomki okrajsani, ker ze tole deluje
