import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def solve():
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))

    cur_sum = 0
    maxi_1 = []
    mini_1 = []
    # print("TEST")
    # print(arr)
    for i, num in enumerate(arr):
        if num == 1:
            heappush(maxi_1, -i)
            heappush(mini_1, i)
        cur_sum += num

    for i in range(q):
        temp = list(map(int, input().split()))
        # print(temp)
        if temp[0] == 1:
            # print(maxi_1, mini_1)
            # print(arr)
            while len(maxi_1) > 0:
                maxi_ele = heappop(maxi_1)
                if arr[-maxi_ele] == 1:
                    heappush(maxi_1, maxi_ele)
                    break
            
            while len(mini_1) > 0:
                mini_ele = heappop(mini_1)
                if arr[mini_ele] == 1:
                    heappush(mini_1, mini_ele)
                    break
            
            if len(maxi_1) == 0:
                if temp[1] % 2 == 0 and temp[1] <= cur_sum:
                    print("YES")
                else:
                    print("NO")
                continue
            # print(mini_ele, maxi_ele)
            if cur_sum - mini_ele * 2 <= cur_sum - (n + maxi_ele - 1) * 2:
                possible_sum = cur_sum - (n + maxi_ele - 1) * 2
            else:
                possible_sum = cur_sum - mini_ele * 2
            # print("possible sum", possible_sum)
            if temp[1] <= possible_sum:
                print("YES")
            elif (temp[1] - possible_sum) % 2 == 0 and temp[1] <= cur_sum:
                print("YES")
            else:
                print("NO")
        else:
            if temp[2] == 1:
                if arr[temp[1] - 1] != 1:
                    heappush(maxi_1, -(temp[1]-1))
                    heappush(mini_1, (temp[1]-1))
            cur_sum = cur_sum + temp[2] - arr[temp[1] -1]
            arr[temp[1]-1] = temp[2]


        
for t in range(int(input())):
    solve()