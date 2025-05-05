from heapq import heappop, heappush, heapify

def solve(n, k, a, b):
    arr = [(a[i], b[i]) for i in range(n)]

    arr.sort(key=lambda x: x[0])
    # print(arr)
    heap = []
    maxi = -1
    for i in range(n):
        while len(heap) > 0:
            if heap[0] < arr[i][0]:
                heappop(heap)
            else:
                break
        if len(heap) <= k:
            maxi = max(maxi, (n - i) * arr[i][0] + len(heap) * arr[i][0])
        # print(heap, arr[i][0])
        heappush(heap, arr[i][1])
    # print(maxi)
    # print("second")
    arr.sort(key=lambda x: x[1])
    # print(arr)
    heap = a
    heapify(heap)
    per = -1
    for i in range(n):
        if arr[i][1] != per:
            while len(heap) > 0:
                if heap[0] < arr[i][1]:
                    heappop(heap)
                else:
                    break
            if n - len(heap) - i <= k:
                maxi = max(maxi, (n - i) * arr[i][1])
            # print(heap, arr[i][1])
        per = arr[i][1]
    print(maxi)
    # return maxi


def brute(n, k, a, b):
    maxi = -1
    for i in range(min(a), max(b) + 1):
        count = 0
        ans = 0
        for j in range(n):
            if i <= a[j]:
                ans += i
            elif i > a[j] and i <= b[j]:
                ans += i
                count += 1
        if count <= k:
            maxi = max(maxi, ans)
    return maxi

from random import randint

def check():
    n = 5
    k = 3
    for i in range(10000):
        a = []
        b = []
        for i in range(n):
            temp = randint(1, 20)
            a.append(temp)
            b.append(temp + randint(1, 20))
        # print(a, b)
        if solve(n, k, a[:], b[:]) != brute(n, k, a[:], b[:]):
            print("Found")
            print(n, k)
            print(a)
            print(b)
            print(brute(n, k, a,b))
            exit()



# check()
for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(n, k, a, b)