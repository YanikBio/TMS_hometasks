import random as r
import copy

def create_matrix(m, n):
    matrix = [[int(r.random() * 10) for a in range(n)] for b in range(m)]
    return matrix

def sum_matrix_Lline(matrix, L):
    num_line = copy.copy(matrix[L])
    d = 0
    for a in range(len(matrix)):
        #print(matrix[a], end='<- here\n')
        #print(num_line, end='<- and here\n')
        for b in range(len(matrix[0])):
            matrix[a][b] = matrix[a][b] + num_line[b]

    return matrix

def show_info(info):
    for line in info:
        print(line)
    print()

def user_input():
    m, n, L = map(int, input().split())
    return m, n, L

def main():
    m, n, L = user_input()
    matrix = create_matrix(m, n)
    show_info(matrix)
    matrix = sum_matrix_Lline(matrix, L)
    show_info(matrix)

if __name__ == '__main__':
    main()