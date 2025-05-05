def main():
    t = int(input())
    for i in range(t):
        n, k ,b, s = list(map(int, input().split()))
        temp1 = s - k * b
        if k - 1 == 0:
            if b == s:
                print(s, end = " ")
                for i in range(n-1):
                    print(0, end=" ")
                print()
            else:
                print(-1)
            continue
        if temp1 / (k - 1) <= n and temp1 / (k - 1) >= 0:
            if s >= b*k + k - 1:
                print(b * k + k - 1, end=" ")
                temp = b * k + k - 1
            else:
                print(b * k, end=" ")
                temp = b * k
            for i in range(n-1):
                if s - temp >= k-1:
                    print(k-1, end = " ")
                    temp = temp + (k-1)
                else:
                    print(s - temp, end = " ")
                    temp = temp + (s - temp)
            print()
        else:
            print(-1)

main()