def solve():
    n, l, r = map(int, input().split())

    arr = list(map(int, input().split()))
    
    temp1 = arr[:r]
    temp2 = arr[l-1:]
    temp1.sort()
    temp2.sort()
    print(min(sum(temp1[:(r-l+1)]), sum(temp2[:(r-l+1)])))
for t in range(int(input())):
    solve()