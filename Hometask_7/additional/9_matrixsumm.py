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

def matrix_sum(matrix):
    summa_of_matrix = 0
    lenght_m = len(matrix)
    lenght_n = len(matrix[0])

    summa_of_column = []

    for a in range(0, lenght_m):
        for b in range(0, lenght_n):
            summa_of_matrix += matrix[a][b]

    for a in range(0, lenght_m):
        summa_of_column.append(0)
        for b in range(0, lenght_n):
            summa_of_column[a] += matrix[b][a]

    return summa_of_matrix, summa_of_column


matrix = makematrix(3,3)
for line in matrix:
    print(line)
print(matrix_sum(matrix))