import math as m
# print message for user and take from him a chose number
print('Если вы вводите три стороны a, b, c, нажмите \'1\' если стороны a, b и угол С, нажмите \'2\'')
user_input = input()
# loop
while True:
    a, b, c = 0, 0, 0
    cornerC = 0
    R = 0
    S = 0
    # part for finding the angle C
    if int(user_input) == 1:  # why this don't work when user_input == str()?
        print('Введите a, b, c:')
        a, b, c = [int(_) for _ in input().split()]
        if a + b > c and a + c > b and c + b > a:
            cornerC = m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
            cornerC = m.degrees(cornerC)  # m.acos() return value in radians, so... changing in degrees
        else:
            print('Введите корректные значения a, b, c:')
            continue
    # part for finding the side c
    elif int(user_input) == 2:
        print('Введите a, b и угол С')
        a, b, cornerC = [int(_) for _ in input().split()]
        if a > 0 and b > 0 and 0 < cornerC < 180:
            c = (a ** 2 + b ** 2 - (2 * a * b) * (m.cos(m.radians(cornerC)))) ** 0.5
        else:
            print('Введите корректные значения a, b, C:')
            continue

    else:
        print('Вы выбрали некоректные данные, выберите, пожалуйста или 1 или 2')
        user_input = input()
        continue

    R = (((a + b + c) / 2) - c) * m.tan(m.radians(cornerC) / 2)
    S = m.pi * (R ** 2)
    print(f'площадь вписанной окружности равна {S} см^3')
    break

"""
how to find the S with knowing another angles.. 
"""