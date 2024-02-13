'''
при поиски в сдвинутом списке, скорость будет О(n), что равно линейному
поэтому я думаю, что следует все отрезки "сохранять" и идти по ним попорядку...
* как варик, можно внести проверку типа a<b<c таким образом обнаруживать сдвиг и тогда 
двигаться "в него"
'''

search_line = [5, 6, 7, 8, 9, 1, 2, 3, 4]
find_num = 1

low = 0
high = len(search_line) - 1

memory = []

while low <= high:

    mid = (low + high) // 2
    elem = search_line[mid]

    if elem == find_num:
        print(f'Here: {mid}')
        break
    elif find_num < elem:
        high = mid - 1
    elif find_num > elem:
        low = mid + 1
    else:
        print('Нет такого элемента')
