fibonachi = 1
a = 1

user_input = int(input('Сколько вывести чисел: '))

for _ in range(user_input):
    print(fibonachi, end=' ')
    if _ % 10 == 0:
        print()
    fibonachi, a = fibonachi + a, fibonachi