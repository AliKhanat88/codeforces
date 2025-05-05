



def check_least_LCM(num):
    for i in range(2, 100000):
        if num % i == 0:
            print(num // i, num -  num // i)
            return
    print(1, num-1)
            


def main():
    t = int(input())
    for i in range(t):
        num = int(input())
        check_least_LCM(num)

main()
