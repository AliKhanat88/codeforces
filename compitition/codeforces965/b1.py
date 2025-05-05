def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    first = 0 
    last = n - 1
    for i in range(n):
        if arr[i] == brr[first]:
            first += 1
        elif arr[i] == brr[last]:
            last -= 1
        else:
            print("Alice")
            return
    first = 0 
    last = n - 1
    for i in range(n-1, -1, -1):
        if arr[i] == brr[first]:
            first += 1
        elif arr[i] == brr[last]:
            last -= 1
        else:
            print("Alice")
            return
    print("Bob")


for t in range(int(input())):
    solve()