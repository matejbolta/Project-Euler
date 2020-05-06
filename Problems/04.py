'''Find the largest palindrome made from the product of two 3-digit numbers.'''

rezultat = max(i * j       for i in range(100, 1000)      for j in range(100, 1000)      if str(i * j) == str(i * j)[ : : -1])

print(rezultat)