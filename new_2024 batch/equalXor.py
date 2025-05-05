def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    set1 = set(arr[:n])
    set2 = set(arr[n:])
    # print("TEST")
    # print(set1)
    # print(set2)
    ans1 = []
    ans2 = []
    for i in range(1, n+1):
        if i in set1 and i not in set2:
            if len(ans1) < 2*k-1:
                ans1.append(str(i))
                ans1.append(str(i))
        elif i in set2 and i not in set1:
            if len(ans2) < 2*k-1:
                ans2.append(str(i))
                ans2.append(str(i))
    for i in range(1, n+1):
        if i in set1 and i in set2:
            if len(ans1) < 2*k and len(ans2) < 2*k:
                ans1.append(str(i))
                ans2.append(str(i))

    print(" ".join(ans1))
    print(" ".join(ans2))
for t in range(int(input())):
    solve()