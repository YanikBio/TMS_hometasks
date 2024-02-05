'''
не работает для матриц несеметричных, где m > n
'''

import random

def makematrix(m, n):
    
    matrix = []

    for a in range(0, m):
        matrix.append([])
        for b in range(0, n):
            matrix[a].append(int(random.random() * 10 // 1))
            b += 1
        a += 1
        b = 0
    return matrix

def diagonalssumma(matrix):
    main_d_sum = 0
    second_d_sum = 0

    lenght_m = len(matrix)
    lenght_n = len(matrix[0])

    for a in range(lenght_m):
        b = a
        main_d_sum += matrix[a][b]
        second_d_sum += matrix[a][lenght_n - 1 - a]
    
    return main_d_sum, second_d_sum


m = makematrix(4, 3)
for line in m:
    print(line)

print(diagonalssumma(m))