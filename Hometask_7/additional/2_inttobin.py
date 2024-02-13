def inttobin(num):
    bin_num = ''
    while num != 0:
        if num % 2 != 0:
            bin_num += '1'
            num = num // 2
        else:
            bin_num += '0'
            num = num // 2

    return bin_num

def show_info(num):
    print(num)

def user_input():
    num: int = int(input())
    return num

def main():
    int_num = user_input()
    bin_num = inttobin(int_num)
    show_info(bin_num)

if __name__ == '__main__':
    main()