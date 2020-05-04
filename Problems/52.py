'''
Permuted multiples

It can be seen that the number, 125874, and its double,
251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

def st2set(n):
    '''stevke da v mnozico'''
    assert n >= 0 #zakaj pa ne
    stevke = set()
    while n != 0:
        stevke.add(n % 10)
        n //= 10
    return stevke

import itertools
for i in itertools.count(1):
    if st2set(i) == st2set(2*i) == st2set(3*i) == st2set(4*i) == st2set(5*i) == st2set(6*i):
        print(f'tole iščemo: {i}')
        break

#tole iščemo: 142857