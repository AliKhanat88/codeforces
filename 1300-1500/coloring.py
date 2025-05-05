
def solve():
    n, m, k = map(int, input().split())

    arr = [*map(int, input().split())]
    added = n - k * (n // k)
    temp = 0
    for i in range(m):
        if arr[i] > n // k + 1:
            print("NO")
            return
        if arr[i] == n // k + 1:
            temp += 1
    if temp > added:
        print("NO")
        return 
    print("YES")



for t in range(int(input())):
    solve()