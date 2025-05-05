def give_max(x1, q1, x2, q2, k):
    # print(x1, q1, x2, q2, k)
    if x1 * q1 + x2 * q2 <= k:
        return x1 * q1 + x2 * q2
    cur = min(k // x1, q1) * x1
    cur_q1 = q1 - cur // x1
    cur_q2 = q2 - (k - cur) // x2
    cur = cur + (k - cur) // x2 * x2
    maxi = cur + min(k - cur, min(q1 - cur_q1, cur_q2))
    # print(maxi)
    cur = min(k // x2, q2) * x2
    cur_q2 = q2 - cur // x2
    cur_q1 = q1 - (k - cur) // x1
    cur = cur + (k - cur) // x1 * x1
    if cur_q1 >= 1:
        cur += x1
        cur_q1 -= 1
    else:
        cur += x2
        cur_q2 -= 1
    
    if cur - k <= q2 - cur_q2 and cur - k <= cur_q1:
        return k
    return maxi


# print(give_max(207, 4, 206, 3, 1033))


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    crr = list(map(int, input().split()))

    arr = [(arr[i], crr[i]) for i in range(n)]
    arr.sort(key=lambda x: x[0])
    # print(arr)
    maxi = -1
    for i in range(n):
        maxi = max(maxi, min(k // arr[i][0], arr[i][1]) * arr[i][0])
        if i > 0 and arr[i][0] - 1 == arr[i-1][0]:
            maxi = max(maxi, give_max(arr[i-1][0], arr[i-1][1], arr[i][0], arr[i][1], k))

    print(maxi)

for t in range(int(input())):
    solve()
    

    
