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

matrix = makematrix(12, 15)
for line in matrix:
    print(line)