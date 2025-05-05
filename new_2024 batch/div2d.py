def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    if arr[0] != 1:
        print("Alice")
    else:
        start = 1
        count = 0
        i = 0
        while i < n:
            if arr[i] == start:
                count += 1
                start += 1
            elif arr[i] < start:
                pass
            else:
                break
            i += 1
        if i < n:
            if count % 2 == 0:
                print("Alice")
            else:
                print("Bob")
        else:
            if count % 2 == 1:
                print("Alice")
            else:
                print("Bob")

for t in range(int(input())):
    solve()