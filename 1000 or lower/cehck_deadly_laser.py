def main():
    t = int(input())
    for i in range(t):
        n, m , s1, s2, d = map(int, input().split())
        if (d < n-s1 and d < s2 - 1) or (d < s1 - 1 and d < m - s2):
            print(n + m - 2)
        else:
            print(-1)

main()