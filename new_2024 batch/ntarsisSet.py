def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # print("TEST")
    if arr[0] != 1:
        print(1)
        return 

    div = 1
    start = 1
    step = 1
    for i in range(1, n):
        adv = min(k, (arr[i] - start - 1) // step)
        start = start + adv * step
        # print("div step adv k start", div, step, adv, k, start)
        step += 1
        div += 1
        k -= adv
        if k == 0:
            print(start)
            return
    print(start + step * k)
for t in range(int(input())):
    solve()