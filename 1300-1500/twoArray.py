def solve():
    n, t = map(int, input().split())
    arr = [*map(int,input().split())]
    if t % 2 != 0: 
        for i in range(n):
            if arr[i] <= t//2:
                print(0, end=" ")
            else:
                print(1, end=" ")
    if t % 2 == 0: 
        found = 0
        for i in range(n):
            if arr[i] < t//2:
                print(0, end=" ")
            elif arr[i] == t//2:
                print(found,end=" ")
                found = (found + 1) % 2
            else:
                print(1, end=" ")
    print()
for t in range(int(input())):
    solve()