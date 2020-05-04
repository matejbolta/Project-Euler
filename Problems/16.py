#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2 ** 1000?

def vsota_stevk(n):
    if n == 0:
        return 0
    else:
        return n % 10 + vsota_stevk(n // 10)

print(vsota_stevk(2 ** 1000))