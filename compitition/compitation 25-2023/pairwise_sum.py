def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        sum = 0
        for i in range(1, m+1):
            sum += (m-i+1) * (n+i+n+m) / 2
        print(int(sum))

main()