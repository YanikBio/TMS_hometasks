import matplotlib

A = 0  # the user number
n = 0  # the sqrt 

while 1:
    A = int(input("Введите число: "))
    n = int(input("Введите степень корня: "))

    if n % 2 == 0 and A < 0: 
        print("У отрицательного числа не может быть чётного корня. Введите корректные данные.")
    elif n == 0:
        print("Степень корня не может быть равна нулю. Введите корректные данные.")
    else:
        break

x = 2
x1 = 0

crutch = 0 
if n < -1:  
    crutch = n  # crutch for n < 0 
    n = n * -1

while 1:
    if n == 1:
        print(f"Арифметическим корнем степени {n} числа {A} является само число {A} ")  # exception with sqrt = 1
        break
    if A == 0:
        print(f"Любой корень числа {A} равен самому {A} ")  # exception for 0
        break
    if n == -1:
        print(f"Любой корень числа {A} равен обратному числу {A}, то есть {1/A} ")
        break

    x1 = 1/n * ((n-1) * x + (A / (x**(n-1))))
    if round(x, 3) == round(x1, 3) and crutch < 0:  # crutch!!! (костыли - наше всё!)
        print(f"Арифметическим корнем степени {n} числа {A} является {round((1/x1), 4)}")
        break
    elif round(x, 3) == round(x1, 3):
        print(f"Арифметическим корнем степени {n} числа {A} является {round(x1, 4)} ")  # show the answer
        break

    else:
        x = x1
