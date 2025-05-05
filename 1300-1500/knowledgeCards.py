def solve():
    n,m,k = map(int, input().split())
    arr = input().split()
    arr = [(i, int(arr[i])) for  i in range(k)]

    arr.sort(key=lambda x: x[1], reverse=True)
    temp = n * m - 2 - 2
    for i in range(k):
        if arr[i][0] - i > temp:
            print("TIDAK")
            return
    print("YA")




for t in range(int(input())):
    solve()