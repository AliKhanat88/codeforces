from collections import defaultdict
from math import isqrt
num = 300001
prime = [True] * (num)
for i in range(2, int(isqrt(num)) + 1):

    for j in range(i + i, num, i):
        prime[j] = False

primes = []
for i in range(2, num):
    if prime[i] == True:
        primes.append(i)


def compute_oper(x):
    if x % 2 == 1:
        return (((x - 1)  // 2) * (x) + x + 1)
    return (((x - 1)  // 2) * (x) + x + 2)


def solve(n):
    
    lower = 1
    upper = len(primes)
    while upper - lower > 1:
        mid = lower + (upper - lower) // 2
        if compute_oper(mid) >= n:
            upper = mid
        else:
            lower = mid + 1
    if compute_oper(lower) >= n:
        count = lower
    elif compute_oper(upper) >= n:
        count = upper
    else:
        raise Exception()
    # print(count)
    ans = [0] * n

    graph = [set([i for i in range(count)]) for i in range(count)]
    stack = []
    if (count - 1) % 2 == 1:
        for i in range(1, count-1, 2):
            graph[i].remove(i+1)
            graph[i+1].remove(i)

    ans = []

    cur = 0

    while stack or graph[cur]:
        if not graph[cur]:
            ans.append(cur)
            cur = stack.pop()
        else:
            stack.append(cur)

            nxt = graph[cur].pop()
            # print(nxt)
            if cur in graph[nxt]:
                graph[nxt].remove(cur)
            cur = nxt
    ans.append(cur)
    # print(ans)
    print(*[primes[ans[i]] for i in range(n)])
    # return [primes[ans[i]] for i in range(n)]


if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        solve(n)