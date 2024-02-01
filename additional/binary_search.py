# как находить позицию элемента???

sorted_list = sorted([1, 2, 3, 4, 6, 7, 8, 9])
finding_elem = 9

mid = int(len(sorted_list) / 2) - 1
left_list = sorted_list[:mid]
right_list = sorted_list[mid:]

answer = mid

while 1:

    print(mid)
    print(sorted_list[mid])
    print(left_list)
    print(right_list)

    if finding_elem == sorted_list[mid]:
        print(f'here - {answer}')
        break
    
    elif finding_elem < left_list[-1]:
        sorted_list = left_list
        mid = int(len(sorted_list) / 2)
        left_list = sorted_list[:mid]
        right_list = sorted_list[mid:]
    
    elif finding_elem > right_list[0]:
        sorted_list = right_list
        mid = int(len(sorted_list) / 2)
        left_list = sorted_list[:mid]
        right_list = sorted_list[mid:]

    else:
        break
    