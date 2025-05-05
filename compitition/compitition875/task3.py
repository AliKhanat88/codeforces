from collections import defaultdict
def solve():
    n = int(input())
    arr = list(range(1, n+1))
    dict = defaultdict(lambda:[])
    dict_time = defaultdict(lambda:[])
    for i in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict_time[a].append(i)
        dict[b].append(a)
        dict_time[b].append(i)


    reading = 0
    new_stack = [(1, -1)]
    arr[0] = -1
    for i in range(n):
        while arr[i] != -1:
            reading += 1
            stack = new_stack
            new_stack = []
            while len(stack) != 0:
                cur = stack.pop(-1)
                length = len(dict[cur[0]]) - 1
                for j in range(length, -1, -1):
                    if dict_time[cur[0]][j] >= cur[1]:
                        temp_time = dict_time[cur[0]].pop(j)
                        temp = dict[cur[0]].pop(j)
                        stack.append((temp, temp_time))
                        new_stack.append((temp, -1))
                        arr[temp-1] = -1     
    print(reading)

for t in range(int(input())):
    solve()