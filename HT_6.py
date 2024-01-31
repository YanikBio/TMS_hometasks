A = 265
n = 9

x = 2

while x < A:
    x1 = 1/n * ((n-1) * x + (A / (x**(n-1))))
    print(round(x1, 4))
    if round(x, 3) == round(x1, 3):
        break
    else:
        x = x1