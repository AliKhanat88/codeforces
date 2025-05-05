def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        r = ""
        temp = n - k - 1
        for i in range(temp//2, n - temp//2):
            r += f"{i} "
        print(r)

main()