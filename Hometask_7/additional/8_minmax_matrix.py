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

def findinmatrix(matrix):
    max_num = matrix[0][0]
    min_num = matrix[0][0]
    length_m = len(matrix)
    lenght_n = len(matrix[0])

    for a in range(0, length_m-1):
        for b in range(0, lenght_n-1):
            if matrix[a][b] > max_num:
                max_num = matrix[a][b]
            if matrix[a][b] < min_num:
                min_num = matrix[a][b]

    return f'cамое большое число: {max_num}, самое маленькое число: {min_num}'


matrix = makematrix(5,7)

for line in matrix:
    print(line)

print(findinmatrix(matrix))