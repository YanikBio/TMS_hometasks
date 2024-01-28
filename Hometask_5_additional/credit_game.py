"""
m – ежемесячная выплата
i – годовая процентная ставка
p – месячная процентная ставка
s – сумма займа
n – количество месяцев, на которые взят кредит
"""
i = int(input("годовая процентная ставка: ")) / 100
p = int(input("месячная процентная ставка: ")) / 100
s = int(input("сумма займа: "))
n = int(input("количество месяцев, на которые взят кредит: "))

m = (s * p * (1+p)**n) / ((1 + p)**n - 1)
m = round(m, 3)
print(f"Ежемесячная выплата составит: {m} рублей")
summa = m * n + s
print(f"Вы всего заплатите банку {summa} рублей")
overpayment = summa - s
print(f"Вы всего переплатите банку {overpayment} рублей")

