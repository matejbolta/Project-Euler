def najmanjsi_prafaktor_od(n):
	for x in range(2, n + 1):
		if n % x == 0:
			return x


najmanjsi_prafaktor_od(25)  #deluje :)




n = 600851475143
while najmanjsi_prafaktor_od(n) < n:
	n = n // najmanjsi_prafaktor_od(n)



print(n)