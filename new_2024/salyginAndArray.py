def query(i):
    print(f"? {i}", flush=True)
    return int(input())

def solve():
    n, k = map(int, input().split())

    ans = 0
    i = 1
    while i + 2 * k - 1 <= n:
        ans = ans ^ query(i)
        i += k
    if n % k == 0:
        ans = ans ^ query(n - k + 1)
        print(f"! {ans}")
    else:
        start = n - k - n % k + 1
        ans = ans ^ query(start)
        ans = ans ^ query(start + (n % k) // 2)
        ans = ans ^ query(n - k + 1)
        print(f"! {ans}")

for t in range(int(input())):
    solve()