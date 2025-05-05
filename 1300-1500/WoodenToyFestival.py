from math import ceil

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n <= 3:
        print(0)
        return
    arr.sort()
    mini = arr[-1] - arr[0]
    for i in range(n-1):
            temp1 = abs(arr[i] - arr[0])
            if temp1 > mini:
                break
            for j in range(i+1, n-1):
                temp2 = abs(arr[j] - arr[i+1])
                temp3 = abs(arr[n-1] - arr[j+1])
                if temp2 > mini:
                    break
                mini = min(mini, max(temp1, temp2, temp3))
    print(ceil(mini / 2))

for t in range(int(input())):
     solve()