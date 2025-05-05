def solve():
    n, m = map(int, input().split())
    print("? 1 1", flush=True)
    a = int(input())
    if a < n - 1:
        r1 = 1 + a
        c1 = 1
    else:
        r1 = n
        c1 = a - (n - 1) + 1

    print(f"? {n} 1", flush=True)
    b = int(input())
    if b < m - 1:
        r2 = n
        c2 = b + 1
    else:
        r2 = b - (m - 1) + 1
        c2 = m

    print(f"? {n} {m}", flush=True)
    c = int(input())
    if c < m - 1:
        r3 = n
        c3 = c + 1
    else:
        c3 = 1
        r3 = c - (m-1) + 1
    common_column = abs(c2 - c1) // 2 + c1
    if r2 - (c2 - common_column) == r1 - (c1 - common_column):
        common_a_b_x = r2 - (c2 - common_column)
        common_a_b_y = common_column

    common_column = (c3 - c1) // 2

    
for t in range(int(input())):
    solve()
