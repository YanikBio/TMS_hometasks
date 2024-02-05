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

def findthenum(matrix, h):

    lenght_m = len(matrix)
    lenght_n = len(matrix[0])
    here = []
    not_here = []

    for a in range(0, lenght_m):
        for b in range(0, lenght_n):
            if h == matrix[b][a]:
                here.append(a+1)
                break
        else: 
            not_here.append(a+1)

    return here, not_here

matrix = makematrix(5,5)
h = 3
for line in matrix:
    print(line)

return_from = findthenum(matrix, h)
here = return_from[0]
not_here = return_from[1]

print('Данные столбцы {} имеют в своём составе хоть одно число {}'.format(', '.join(str(i) for i in here), h))
print('В то время как столбы {} не имеют в своём составе этого числа'. format(', '.join(str(i) for i in not_here)))
