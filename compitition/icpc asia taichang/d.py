import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solve():
    n, m = map(int, input().strip().split())
    arr = [0] * n
    start = None
    end = None
    for i in range(n):
        arr[i] = input().strip()
        temp_s = arr[i].find("S")
        if temp_s != -1:
            start = (i, temp_s)
        temp_t = arr[i].find("T")
        if temp_t != -1:
            end = (i, temp_t)

    assert start != None
    assert end != None
    inf = 10 ** 18
    heap = [(0, start[0], start[1], "n", -1, -1)]
    mini = [[[[inf, inf, inf], [inf, inf, inf], [inf, inf, inf], [inf, inf, inf]] for i in range(m)] for i in range(n)]
    mini[start[0]][start[1]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    moves = [(-1, 0, "t"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
    dict = {
        "t": 0,
        "d": 1,
        "l": 2,
        "r": 3,
        "n": 0,
    }
    # print("start", start)
    # print("end", end)
    while heap:
        cur = heappop(heap)
        if mini[cur[1]][cur[2]][dict[cur[3]]][cur[4]] == cur[0]:
            # print(cur)
            if cur[1] == end[0] and cur[2] == end[1]:
                print(cur[0])
                return
            for i, move in enumerate(moves):
                new_i, new_j = cur[1] + move[0], cur[2] + move[1]
                if arr[new_i][new_j] != "#":
                    if cur[3] == move[2]:
                        if cur[4] >= 2:
                            continue
                        else:
                            new_dist  = cur[0] + 1
                            cont_dir = cur[4] + 1
                    else:
                        new_dist = cur[0] + 1
                        cont_dir = 0

                    if mini[new_i][new_j][dict[move[2]]][cont_dir] > new_dist:
                        mini[new_i][new_j][dict[move[2]]][cont_dir] = new_dist
                        heappush(heap, (new_dist, new_i, new_j, move[2], cont_dir, cur[0], cur[1], cur[2], cur[3], cur[4]))
        
    print(-1)
    # new_min = inf
    # for i in range(4):
    #     new_min = min(new_min, min(mini[end[0]][end[1]][i]))
    # if new_min == inf:
    #     print(-1)
    # else:
    #     print(new_min)
                    
                    





        





solve()