'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def vsota_5(n):
    if n < 10:
        return n ** 5
    return (n % 10) ** 5 + vsota_5(n // 10)

def ustrezna(n):
    return n == vsota_5(n)

seznam = []
for i in range(2, 10 ** 6):
    if ustrezna(i):
        seznam.append(i)

print(sum(seznam))
#10 ** 6: 443840
#očitno je do milijon dovolj.
#443839
