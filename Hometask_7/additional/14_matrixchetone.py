import random

def create_matrix(m, n):
    matrix = []
    for a in range(m):
        matrix.append([])
        for b in range(n):
            el = random.random()
            if el < 0.5:
                el = 0
            else: 
                el = 1

            matrix[a].append(el)
    return matrix

def add_line(matrix: list):
    n = 0
    for line in matrix:
        if line.count(1) % 2 == 0:
            matrix[n].append(0)
            n += 1
        else:
            matrix[n].append(1)
            n += 1
    
    return matrix

def user_input():
    m, n = map(int, input().split())
    return m, n

def show_matrix(matrix):
    for line in matrix:
        print(line)

def main():
    m, n = user_input()
    matrix = create_matrix(m, n)
    show_matrix(matrix)
    matrix = add_line(matrix)
    show_matrix(matrix)

if __name__ == "__main__":
    main()