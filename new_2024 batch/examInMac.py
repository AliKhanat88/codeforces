def solve():
    n, c = map(int, input().split())

    arr = list(map(int, input().split()))
    print("TEST")
    even = 0
    odd = 0
    if arr[0] != 0:
        even += 1
    if arr[-1] != c:
        if c % 2 == 1:
            odd += 1
        else:
            even += 1
    arr.append(c)
    arr.insert(0, 0)
    print(arr, c)
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            if (arr[i] - arr[i-1] - 1) % 2 == 1:
                if arr[i-1] % 2 == 0:
                    odd += 1
                else:
                    even += 1
            even += (arr[i] - arr[i-1] - 1) // 2
            odd += (arr[i] - arr[i-1] - 1) // 2

    new_odd = 0
    new_even = 0
    if c % 2 == 1:
        new_even += 1
    new_even += (c // 2)
    new_odd += (c // 2)
    print(odd, even, new_even, new_odd)
    ans = new_odd * odd + new_even * even + (odd * (odd + 1) // 2) + (even * (even + 1) // 2)
    print(ans)

for t in range(int(input())):
    solve()