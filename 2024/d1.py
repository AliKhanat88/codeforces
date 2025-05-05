import sys
input = sys.stdin.readline
inf = 99999999999999999999999999999
from collections import defaultdict

oppo = {
    "BG" : "RY", 
    "BR": "GY", 
    "BY": "GR",
    "GR":"BY",
    "GY": "BR",
    "RY": "BG"
}

def solve():
    n, q = map(int, input().split())
    arr = list(input().strip().split())
    left = [-1] * n
    right = [inf] * n

    dict = defaultdict(lambda:None)
    for i in range(n):
        maxi = -1
        for key, val in dict.items():
            if key != arr[i] and dict[key] != None and key != oppo[arr[i]]:
                maxi = max(maxi, val)
        left[i] = maxi
        dict[arr[i]] = i

    dict = defaultdict(lambda:None)
    for i in range(n-1, -1, -1):
        mini = inf
        for key, val in dict.items():
            if key != arr[i] and dict[key] != None and key != oppo[arr[i]]:
                mini = min(mini, val)
        right[i] = mini
        dict[arr[i]] = i

    # print(left)
    # print(right)

    for i in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        if oppo[arr[a]] != arr[b]:
            print(b - a)
        else:
            if left[b] == -1:
                mini = inf
            elif left[b] >= a:
                mini = b - a
            else:
                mini = b - a + (a - left[b]) * 2
            # print("HERE")
            # print(mini)
            if right[b] != inf:
                mini = min(mini, b - a + (right[b] - b) * 2)
            
            if left[a] == -1:
                pass
            else:
                mini = min(mini, a - left[a] + b - left[a])
            # print("HERE")
            # print(mini)
            if right[a] != inf:
                if right[a] <= b:
                    mini = min(mini, b - a)
                else:
                    mini = min(mini, right[b] - a + right[b] - b)


            if mini < 10000000000 and mini > 0:
                print(mini)
            else:
                print(-1)


for t in range(int(input())):
    solve()