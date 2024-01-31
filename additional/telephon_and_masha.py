cost_of_the_phone = int(input("Сколько стоит телефон: "))
masha_money = 0
masha_salary = int(input("Сколько откладыавет Маша: "))

day_count = 0

while masha_money < cost_of_the_phone:
    day_count += 1
    if day_count % 7 == 0:
        continue
    else:
        masha_money += masha_salary
    
print(day_count)