def solve():
    n,m,k = map(int, input().split())

    s = input().split()
    staged = input().split()
    last = input().split()

    stages_k = 0
    for file in staged:
        if file in last:
            stages_k += 1
    mini = min(k + 1, n - k + 1)
    mini = min(mini, len(staged) - stages_k + (k - stages_k))
    print(mini)
for t in range(int(input())):
    solve()