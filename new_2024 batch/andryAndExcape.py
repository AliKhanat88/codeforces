from bisect import bisect_right
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    # print("TEST")
    points = []

    for i in range(n):
        l,r,a,b = map(int, input().split())
        points.append((l, b))

    points.sort()
    # print(points)

    q = int(input())
    temp_q = input().split()
    ques = [[int(temp_q[i]), i] for i in range(q)]
    ques.sort()
    ans = 0
    last = 0
    for i in range(q):
        if ans >= ques[i][0]:
            ques[i][0] = ans
            continue
        ans = ques[i][0]
        while last < len(points):
            if points[last][0] <= ans:
                ans = max(ans, points[last][1])
            else:
                break
            last += 1
        ques[i][0] = ans
    ans_arr = [0] * q
    for num in ques:
        ans_arr[num[1]] = num[0]
    print(*ans_arr)
for t in range(int(input())):
    solve()