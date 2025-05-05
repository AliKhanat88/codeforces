inf = 1000000000

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    per1 = inf
    per2 = inf
    count = 0 
    for num in arr:
        if num > per1 and num < per2:
            count += 1
            per2 = num
        if num < per1:
            per1 = num
    print(count)

for t in range(int(input())):
    solve()
        