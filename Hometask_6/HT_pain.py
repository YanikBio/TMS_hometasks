A_list = [i for i in range(5, 10000, 20)]
answer = []
itaration = []

while A_list != []:
    A = A_list[0]
    A_list.pop(0)
    n = 10
    #n = n_list[0]
    #n_list.pop(0)

    x = 2
    x1 = 0

    count = 0

    while 1:
        count += 1
        x1 = 1/n * ((n-1) * x + (A / (x**(n-1))))
        #x1 = 1/n * ((n-1) * (1/n * ((n-1) * x + (A / (x**(n-1))))) + (A / ((1/n * ((n-1) * x + (A / (x**(n-1)))))**(n-1))))
        if round(x, 3) == round(x1, 3):
            answer.append(round(x1, 3))
            itaration.append(count)
            count = 0
            break

        else:
            x = x1

#print(answer)
print(f'for {n} number or itaration: {itaration}')