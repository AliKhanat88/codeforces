def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    seti = set()
    for i in range(n):
        for j in range(i, n):
            seti.add(arr[i] - arr[j])
            seti.add(arr[i] + arr[j])
            seti.add(-arr[i] + arr[j])
            seti.add(-arr[i] - arr[j])
    print(sorted(list(seti)))


for t in range(int(input())):
    solve()