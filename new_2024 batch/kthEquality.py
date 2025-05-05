def solve():
    a, b, c, k = map(int, input().split())
    if a > c or b > c:
        print(-1)
        return
    # print("test")
    # print(a, b , c)
    start = max(10 ** (a-1), 10 ** (c-1) - 10 ** (b) + 1)
    # print("start:", start)
    # i = 5
    while start < 10 ** a:
        # if i < 0:
        #     break
        second_start = max(10 ** (b-1), 10 ** (c-1) - start)
        second_end = min(10 ** (b) - 1, 10 ** (c) - 1 - start)
        if k <= second_end - second_start + 1:
            print(f"{start} + {second_start + k - 1} = {start + second_start + k - 1}")
            return
        else:
            k = k - (second_end - second_start + 1)
        # print(start, second_start, second_end)
        start += 1
        # i -= 1
    print(-1)
for t in range(int(input())):
    solve()