'''Find the difference between the sum of the
squares of the first one hundred natural
numbers and the square of the sum.'''


a = (sum(range(101))) ** 2

b = 0
for x in range(1, 101):
    b += x ** 2


x = abs(b - a)




print(x)