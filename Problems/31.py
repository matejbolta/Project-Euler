'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

#delamo se, da delamo število N

#N iz 1p : 1 način
def enka(n):  #v prihodnje bo tudi enka(0) = 1, saj se bo tako izšlo. namreč (0) pomeni npr same petke, same desetke,...
    return 1

#N iz 1p 2p : N // 2
def dvojka(n):
    nacini = 0
    for i in range((n // 2) +1):
        nacini += enka(n - 2*i)
    return nacini

#N iz 1p 2p 5p: vsota(i od 0 do vkl. 40) ((N - 5 * i) // 2)
def petka(n):
    nacini = 0
    for i in range((n // 5) +1):
        nacini += dvojka(n - 5*i)
    return nacini

#N iz 1p 2p 5p 10p
def desetka(n):
    nacini = 0
    for i in range((n // 10) +1):
        nacini += petka(n - 10*i)
    return nacini

#n iz 1p ... 20p
def dvajsetka(n):
    nacini = 0
    for i in range((n // 20) +1):
        nacini += desetka(n - 20*i)
    return nacini

#N iz 1p ... 50p
def petdesetka(n):
    nacini = 0
    for i in range((n // 50) +1):
        nacini += dvajsetka(n - 50*i)
    return nacini

#N iz 1p ... 100p
def stotka(n):
    nacini = 0
    for i in range((n // 100) +1):
        nacini += petdesetka(n - 100*i)
    return nacini

#N iz 1p ... 200p
def dvestotka(n):
    nacini = 0
    for i in range((n // 200) +1):
        nacini += stotka(n - 200*i)
    return nacini

print(dvestotka(200))
#73682
