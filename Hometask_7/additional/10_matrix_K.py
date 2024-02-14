import random as r

def create_matrix(m, n):
    matrix = []
    for a in range(m):
        matrix.append([])
        for b in range(n):
            num = int(r.random() * 10)
            matrix[a].append(num)

    return matrix

def matrix_multiply_on_K(matrix, k):
    k_line = []
    for a in range(len(matrix)):
        matrix[a] = [(i * matrix[a][k]) for i in matrix[a]]

    return matrix

def show_info(info):
    for show in info:
        print(show)

def user_input():
    m, n, k = map(int, input().split())
    return m, n, k

def main():
    m, n, k = user_input()
    matrix = create_matrix(m, n)
    show_info(matrix)
    matrix = matrix_multiply_on_K(matrix, k)
    show_info(matrix)

if __name__== "__main__":
    main()