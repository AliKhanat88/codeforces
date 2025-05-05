from collections import deque
def solve(n, m, a, b):
    
    count = 0
    while (n > 1 and m > 0) or (n > 0 and m > 1):
        if n >= m:
            n -= 2
            m -= 1
        else:
            m -= 2
            n -= 1
        count += 1
    

    a = deque(sorted(a))
    b = deque(sorted(b))
    # print("TEST")
    # print(a)
    # print(b)
    # print(count)
    last_a = []
    last_b = []

    ans = []
    cur_maxi = 0
    for i in range(count):
        maxi1=-1;maxi2=-1
        if len(a) - len(last_b) > 1 and len(b) - len(last_a) > 0:
            maxi1 = a[-1] - a[0]
        if len(b) - len(last_a) > 1 and len(a) - len(last_b) > 0:
            maxi2 = b[-1] - b[0]
        # print(maxi1, maxi2, "maxi")
        if maxi1 != -1 or maxi2 != -1:
            if maxi1 >= maxi2:
                last_a.append((a.popleft(), a.pop()))
                cur_maxi += maxi1
            else:
                last_b.append((b.popleft(), b.pop()))
                cur_maxi += maxi2
        else: 
            if len(a) - len(last_b) <= 1:
                tempi, tempj = last_a.pop()
                cur_maxi -= (tempj - tempi)
                cur_maxi += (b[-1] - b[0])
                last_b.append((b.popleft(), b.pop()))
                cur_maxi += (b[-1] - b[0])
                last_b.append((b.popleft(), b.pop()))
            else:
                tempi, tempj = last_b.pop()
                cur_maxi -= (tempj - tempi)
                cur_maxi += (a[-1] - a[0])
                last_a.append((a.popleft(), a.pop()))
                cur_maxi += (a[-1] - a[0])
                last_a.append((a.popleft(), a.pop()))
        # print("iter", i)
        # print(a)
        # print(last_a)
        # print(b)
        # print(last_b)
        ans.append(cur_maxi)
    print(len(ans))
    print(*ans)

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(n, m, a, b)
from random import randint
def checker():
    for i in range(100):
        n = randint(1, 10)
        m = randint(1, 10)
        print(n, m)
        arr1 = [randint(-100, 100) for i in range(n)]
        arr2 = [randint(-100, 100) for i in range(m)]
        print(*arr1)
        print(*arr2)
        solve(n, m, arr1, arr2)

# checker()