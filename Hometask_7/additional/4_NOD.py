def nod(num1, num2):
    if num1 > num2:
        s_num = num2
        l_num = num1
    elif num1 < num2:
        s_num = num1
        l_num = num2
    else:
        return 'Эти числа равны'
    
    for num in range(s_num-1, 0, -1):
        if l_num % s_num == 0:
            return f'NOD is {s_num}'
        elif s_num % num == 0 and l_num % num == 0:
            return f'NOD is {num}'

num1, num2 = map(int, input('Введите два числа: ').split())
print(nod(num1, num2))
