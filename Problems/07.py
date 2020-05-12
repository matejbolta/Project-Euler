'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

# def je_deljivo_s_katerim_od(n, seznam):
#     if seznam == []:
#         return False
#     else:
#         return n % seznam[0] == 0 or je_deljivo_s_katerim_od(n, seznam[1:])
#
# def prastevila_do(n):
#     if n <= 1:
#         return []
#     elif je_deljivo_s_katerim_od(n, prastevila_do(n - 1)):
#         return prastevila_do(n - 1)
#     else:
#         return prastevila_do(n - 1) + [n]
#
# x = prastevila_do(10 ** 6)
#
# print(x[1001])
#
# #presežemo rekurzijo, vendar bi to moglo delovati.

def prime(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else: #vsa liha ostanejo
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

zaporedno = 0
n = 2
while True:
    if prime(n):
        zaporedno += 1
    if zaporedno == 10001:
        print(n)
        break
    n += 1
