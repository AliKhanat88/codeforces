from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    arr = list(map(int,input().split()))

    dict = defaultdict(lambda:0)
    num = n-1
    while True:
        if k == 0:
            print("Yes")
            return 
        if arr[num] > n:
            print("No")
            return 
        if dict[num] == 1:
            print("Yes")
            return 
        dict[num]= 1
        num -= arr[num]
        if num < 0:
            num = n + num
        k -= 1
for t in range(int(input())):
    solve()