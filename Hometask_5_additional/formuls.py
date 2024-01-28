from math import sqrt, sin, cos, radians

print('Введите значения a, b, x через пробелы: ')
a, b, x = input().split()  # you can use map(int, input().split())
print('Отлично! А теперь, выберите какие формулы вы бы хотели вычислить?\
      Напишите через пробел номера формул (1, 2, 3, 4)')
a, b, x = int(a), int(b), int(x)
user_choose = [int(_) for _ in input().split()]

answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0

if 1 in user_choose:
    answer1 = ((a**2) / 3) + (a**2 + 4)/b + (sqrt(a**2 + 4)) / 4 + (sqrt(a**2 + 4)**3) / 4
    print('Ответ на первую формулу:', round(answer1, 3))

if 2 in user_choose:
    answer2 = (cos(radians(x**2))**2 + sin(radians(2 * x - 1))**2)**(1/3)
    print('Ответ на вторую формулу:', round(answer2, 3))

if 3 in user_choose:
    answer3 = cos(radians(x)) + sin(radians(x))
    print('Ответ на третью формулу:',round(answer3, 3))

if 4 in user_choose:
    answer4 = 5 * x + (3 * x**2) * sqrt(1 + sin(radians(x))**2)
    print('Ответ на четвёртую1 формулу:',round(answer4, 3))