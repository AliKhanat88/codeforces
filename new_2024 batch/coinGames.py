def solve():
    n = int(input())

    s = input()
    if n == 1:
        if s == "U":
            print("YES")
        else:
            print("NO")
        return
    arr = [0] * n
    
    for i in range(n):
        if s[i] == "U":
            arr[i] = True
        else:
            arr[i] = False
    alice = True
    while len(arr) > 2:
        i = 0
        while i < len(arr):
            if arr[i]:
                arr[i-1] = not arr[i-1]
                arr[(i+1) % len(arr)] = not arr[(i+1) % len(arr)]
                arr.pop(i)
                alice = not alice
                break
            i += 1
        if i >= len(arr):
            if alice:
                print("NO")
            else:
                print("YES")
            return
        # print(arr)
    if arr == [True, True] or arr == [False, False]:
        if alice:
            print("NO")
        else:
            print("YES")
    else:
        if alice:
            print("YES")
        else:
            print("NO")
    # print(arr)      


for t in range(int(input())):
    solve()
