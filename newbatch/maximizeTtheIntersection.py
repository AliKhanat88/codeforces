import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    pairs_pair = defaultdict(lambda: -1)
    pairs = [0] * k
    for i in range(k):
        a, b = map(int, input().split())
        pairs_pair[a] = b
        pairs_pair[b] = a
        pairs[i] = sorted([a, b])
    ans = 0
    already_done = defaultdict(lambda: False)
    for i in range(k):
        forward = pairs[i][1] - pairs[i][0] - 1
        backword = 2 * n - pairs[i][1] + pairs[i][0] - 1
        count = 0
        if forward <= backword:
            for j in range(pairs[i][0]+1, pairs[i][1]):
                if pairs_pair[j] == -1:
                    count += 1
                elif pairs_pair[j] > pairs[i][1] or pairs_pair[j] < pairs[i][0]:
                    tup = tuple(sorted([*pairs[i], j, pairs_pair[j]]))
                    if already_done[tup] == False:
                        ans += 1
                    already_done[tup] = True
        else:
            for j in range(pairs[i][1] + 1, 2*n+1):
                if pairs_pair[j] == -1:
                    count += 1
                elif pairs_pair[j] > pairs[i][1] or pairs_pair[j] < pairs[i][0]:
                    continue
                else:
                    tup = tuple(sorted([*pairs[i], j, pairs_pair[j]]))
                    if already_done[tup] == False:
                        ans += 1
                    already_done[tup] = True
            for j in range(1, pairs[i][0]):
                if pairs_pair[j] == -1:
                    count += 1
                elif pairs_pair[j] > pairs[i][1] or pairs_pair[j] < pairs[i][0]:
                    continue
                else:
                    tup = tuple(sorted([*pairs[i], j, pairs_pair[j]]))
                    if already_done[tup] == False:
                        ans += 1
                    already_done[tup] = True
        ans += min(count, 2 * n - 2 * k - count)
    # print(already_done)
    ans = ans + (((n - k) * (n - k - 1)) // 2)
    print(ans)
    


for t in range(int(input())):
    solve()