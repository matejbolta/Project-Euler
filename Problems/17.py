'''
Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

#prazen, da ima 'one' indeks 1 in tako dalje
enobesedne_oz_do_19 = ['', 'one', 'two', 'three', 'four',
                       'five', 'six', 'seven', 'eight', 'nine',
                       'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
					   'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

#prazne pri deseticah da ima 'twenty' indeks 2 in tako dalje.
desetice = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def v_besede_zapise(n):
	if 1 <= n <= 19:
		return enobesedne_oz_do_19[n]
	elif 20 <= n <= 99:
		return desetice[n // 10] + enobesedne_oz_do_19[n % 10]
	elif 100 <= n <= 999:
		return enobesedne_oz_do_19[n // 100] + 'hundred' + (('and' + v_besede_zapise(n % 100)) if (n % 100 != 0) else '')
	elif n == 1000:
		return 'onethousand'
	else:
		return 'angleščina moj doma'


x = sum(len(v_besede_zapise(i)) for i in range(1, 1001))

print(f'x = {x}')
# x = 21124
