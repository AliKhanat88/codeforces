from heapq import heappop, heappush, heapify
from math import ceil


def solve():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # print("TEST")
    temp_arr = [(arr[i], i) for i in range(n)]

    done_arr = [False] * n
    heapify(temp_arr)

    count = ceil(k / m)
    last_round = k % m


    for i in range(count):
        temp = heappop(temp_arr)
        done_arr[temp[1]] = True

    largest = temp
    # print(count, m ,k, last_round)
    # print(arr)
    # print(done_arr)
    # print(largest)
    if last_round == 0:
        last_round = m
    ans = 0
    addi = 0
    for i in range(n):
        if done_arr[i] == True:
            if i == largest[1]:
                ans += (addi + arr[i]) * last_round
                addi += last_round
            else:
                ans += (addi + arr[i]) * m
                addi += m
        # print(addi, ans)
    print(ans)
    



for t in range(int(input())):
    solve()