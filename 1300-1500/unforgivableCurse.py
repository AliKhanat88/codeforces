def solve():
    n, k = map(int, input().split())
    a = input()
    b = input()
    arr = [0] * 26
    for i in range(n):
        if i < k and n - i - 1 < k and a[i] != b[i]:
            print("NO")
            return 
        else:
            arr[ord(a[i]) - ord("a")] += 1
            arr[ord(b[i]) - ord("a")] -= 1
    # print(arr)
    for i in range(26):
        if arr[i] != 0:
            print("NO")
            return 
    print("YES")


for t in range(int(input())):
    solve()