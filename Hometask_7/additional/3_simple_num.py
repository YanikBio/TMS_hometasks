def simplenum(num):
    num = int(num)
    for i in range(num-1, 2, -1):
        if num % i == 0:
            print(i)
            return "Не простое" 
          
    return 'Простое'
    

    
file = open('simple_numbers.txt')
number = [i.strip() for i in file]
number = str(number[0])

for i in number.split(','):
    print(simplenum(i))
