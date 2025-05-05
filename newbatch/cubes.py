def solve():
    n, f, k = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = arr[f-1]
    arr.sort(reverse=True)
    # print(arr, temp)
    if temp in arr[:k] and len(arr) <= k:
        print("YES")
    elif temp in arr[:k] and temp in arr[k:]:
        print("MAYBE")
    elif temp in arr[:k]:
        print("YES")
    else:
        print("NO")


for t in range(int(input())):
    solve()