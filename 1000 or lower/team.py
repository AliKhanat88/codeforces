def main():
    n = int(input())
    count = 0
    for i in range(n):
        a, b, c = map(int, input().split(" "))
        if b & c | a & c | a & b == 1:
            count += 1
    print(count)


main()