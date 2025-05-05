def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr= list(map(int, input().split()))
        or_num = arr[0]
        and_num = arr[0]
        for i in range(1, n):
            or_num = or_num | arr[i]
            and_num = and_num & arr[i]

        print(or_num - and_num)


main()