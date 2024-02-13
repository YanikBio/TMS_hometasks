list_of_numbers = [1,1,2,2,3,3,4,5,6,6,6]
uniq_numers = set(list_of_numbers)

list_of_numbers.sort()

for element in uniq_numers:
    if list_of_numbers.count(element) > 1:
        print(f"Элемент '{element}' встречается в списке {list_of_numbers.count(element)} раз(а)")

