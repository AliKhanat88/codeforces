from collections import deque
import sys

input = sys.stdin.readline

def solve():
    s1 = list(input().strip())
    s2 = list(input().strip())
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    
    queue = deque()
    # print("TEST")
    # print(s1)
    # print(s2)
    t, q = map(int, input().split())
    cur_time = 1
    for i in range(q):
        if len(queue) != 0:
            temp = queue.popleft()
            if temp[0] != cur_time:
                queue.appendleft(temp)
            else:
                if s1[temp[1]] != s2[temp[1]]:
                    diff += 1
        in_temp = list(map(int, input().split()))
        if in_temp[0] == 1:
            queue.append((cur_time + t, in_temp[1]-1))
            if s1[in_temp[1]-1] != s2[in_temp[1]-1]:
                diff -= 1
        elif in_temp[0] == 2:
            cur_fault = 0
            if s1[in_temp[2]-1] != s2[in_temp[2]-1]:
                cur_fault += 1
            if s1[in_temp[4]-1] != s2[in_temp[4]-1]:
                cur_fault += 1

            if in_temp[1] == 1 and in_temp[3] == 1:
                s1[in_temp[2]-1], s1[in_temp[4]-1] = s1[in_temp[4]-1], s1[in_temp[2]-1]
            elif in_temp[1] == 1 and in_temp[3] == 2:
                s1[in_temp[2]-1], s2[in_temp[4]-1] = s2[in_temp[4]-1], s1[in_temp[2]-1]
            elif in_temp[1] == 2 and in_temp[3] == 1:
                s2[in_temp[2]-1], s1[in_temp[4]-1] = s1[in_temp[4]-1], s2[in_temp[2]-1]
            elif in_temp[1] == 2 and in_temp[3] == 2:
                s2[in_temp[2]-1], s2[in_temp[4]-1] = s2[in_temp[4]-1], s2[in_temp[2]-1]

            if s1[in_temp[2]-1] != s2[in_temp[2]-1]:
                cur_fault -= 1
            if s1[in_temp[4]-1] != s2[in_temp[4]-1]:
                cur_fault -= 1
            diff = diff - cur_fault
        elif in_temp[0] == 3:
            if diff == 0:
                print("YES")
            else:
                print("NO")
        # print(in_temp)
        # print(diff)
        cur_time += 1

for t in range(int(input())):
    solve()
