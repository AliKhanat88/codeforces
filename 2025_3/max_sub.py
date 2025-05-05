
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        print(arr[0])
    elif len(arr) == 2:
        print(arr[0] | arr[1])
    else:
        maxi = -1
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    maxi = max(maxi, arr[i] | arr[j] | arr[k])
            
        print(maxi)


solve()