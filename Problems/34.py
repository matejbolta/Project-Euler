'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

def f(x):
    '''vsota fakultet stevk'''
    vsota = 0
    for stevka in str(x):
        vsota += factorial(int(stevka))
    return vsota

def resitev(n):
    '''sesteje vsa curios stevila do vkljucno n'''
    vsota = 0
    for i in range(3, n+1):
        if f(i) == i:
            vsota += i
    return vsota

#resitev(10**5) = 40730
#resitev(10**6) = 40730
#resitev(10**7) = 40730
#ok.


