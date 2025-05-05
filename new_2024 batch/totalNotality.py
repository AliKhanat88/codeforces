def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort(reverse=True)
    
    i = 0
    j = 0
    while i < n and j < m:
        if b[j] >= a[i]:
            print(b[j], end=" ")
            j += 1
        else:
            print(a[i], end=" ")
            i += 1
    if i >= n and j >= m:
        print()
    elif i >= n:
        print(" ".join([str(num) for num in b[j:]]))
    elif j >= m:
        print(" ".join([str(num) for num in a[i:]]))

for t in range(int(input())):
    solve()