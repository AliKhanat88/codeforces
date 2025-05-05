def main():
    n = int(input())

    for i in range(n):
        x = int(input())
        temp = x // 2    
        for i in range(1, temp+1):
            for j in range(temp+i , 0, -temp):
                print(j, end = " ")
        if x % 2 != 0:
            print(x, end = " ")
        print()


main()