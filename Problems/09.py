'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet, for which a + b + c = 1000.
Find the product abc.
'''
#dve enačbi
#a**2 + b**2 = c**2
#a + b + c = 1000

for a in range(1, 1001):
	for b in range(a + 1, 1001):
		c = 1000 - a - b
		if a ** 2 + b ** 2 == c ** 2:
			x = a * b * c

print(x)
