from collections import Counter
def solve():
    a, b, k = map(int, input().split())
    a_arr = [*map(int, input().split())]
    b_arr = [*map(int, input().split())]

    a_c = Counter(a_arr)
    b_c = Counter(b_arr)

    ans = 0
    n = len(a_arr)
    for i in range(n):
        ans = ans - a_c[a_arr[i]] - b_c[b_arr[i]] + 1 + n - i
        a_c[a_arr[i]] -= 1
        b_c[b_arr[i]] -= 1
    print(ans)







for t in range(int(input())):
    solve()