def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n-1, -1, -1):
        k = i+1
        temp = 2 * k - 2
        if temp + 1 > n:
            continue
        can_do = True
        for j in range(k, 0, -1):
            if j < arr[temp]:
                can_do = False
                break
            temp -= 1
        if can_do == True:
            print(k)
            return
    print(0)
for t in range(int(input())):
    solve()
            