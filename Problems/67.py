'''
NOTE: This is a much more difficult version of Problem 18.
'''

import os
#os.getcwd() #UVP_2020
os.chdir('project_euler')
os.chdir('txt_files')

#naredimo a = trikotnik
a = []
with open('p067_triangle.txt', 'r', encoding='utf-8') as in_file:
    for vrstica in in_file:
        vrstica = vrstica.split()
        for i, nizek in enumerate(vrstica):
            vrstica[i] = int(nizek)
        a.append(vrstica)

#skopirano iz 18. problema
for i in range(len(a) - 1)[::-1]:
	for j in range(len(a[i])): #cez vrstico
		a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])

print(a[0][0])
