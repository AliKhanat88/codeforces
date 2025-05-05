def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    org = [i for i in range(1, n +1)]
    ans = []

    for i in range(n-1, -1, -1):
        for j in range(org.index(arr[i]), 0, -1):
            ans.append(f"{org[j]} {org[j-1]}")
            org[j], org[j-1] = org[j-1], org[j]
        for j in range(i):
            ans.append(f"{org[j+1]} {org[j]}")
            org[j], org[j+1] = org[j+1], org[j]
    # print(org)
    print(len(ans))
    print("\n".join(ans))

solve()