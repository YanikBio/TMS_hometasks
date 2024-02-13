'''не понимаю эти формулы'''

import math

# formula a
x = -(int(input('Введите число x: ')))
n = int(input('Введите число n: '))

sinus_x = 0

s = 1
i = 0
while i < n:
    sinus_x += ((x**(s+2)) / math.factorial(s+2))
    s += 2
    i += 1
    x *= -1

sinus_x = x - sinus_x + (-1)**n * (x**(2*n+1)) / (math.factorial(2*n+1))
print(round(sinus_x, 3))