def solve():
    n = int(input())

    s = input()
    c = -1
    for i in range(n):
        if ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
            c += 1
        else:
            break
    for j in range(c+1, n):
        if ord(s[j]) >= ord("0") and ord(s[j]) <= ord("9"):
            print("NO")
            return
    
    arr1 = list(s[:c+1])
    arr2 = list(s[c+1:])
    # print(arr1)
    # print(arr2)
    if arr1 == sorted(arr1) and arr2 == sorted(arr2):
        print("YES")
    else:
        print("NO")

for t in range(int(input())):

    solve()