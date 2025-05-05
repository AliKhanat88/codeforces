def solve():
    n = int(input())
    if n <= 2:
        k = ord("a")
        for i in range(n):
            print(chr(k), end="")
            k += 1
    else:
        for i in range(1, n+1):
            if n % i != 0:
                num = i
                break
        # print(num)
        k = ord("a")
        for i in range(n):
            print(chr(k), end= "")
            k += 1
            if k >= ord("a") + num:
                k = ord("a")
    print()

for t in range(int(input())):
    solve()