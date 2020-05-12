'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

vsota = 0
for i in range(1, 1001):
    vsota += i ** i

print(vsota % 10 ** 10)
#9110846700
