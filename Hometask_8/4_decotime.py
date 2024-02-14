import time as t

def decor(func):
    def work():
        b_work_time = t.time()
        func()
        e_work_time = t.time()
        answer = e_work_time - b_work_time
        print(answer)
    return work

@decor
def func():
    b = 20
    a = 10
    print(b + a)

def main():
    func()

if __name__ == "__main__":
    main()