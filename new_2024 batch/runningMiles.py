from heapq import heappop, heappush

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print('TEST')
    # print(arr)

    new_arr = [0] * n
    minus = n
    for i in range(n):
        new_arr[i] = (-arr[i]+minus, arr[i]) 
        minus -= 1

    # print(new_arr)
    new_maxi_arr = [0] * n
    heap = [new_arr[0]]
    for i in range(1, n):
        temp = heappop(heap)
        new_maxi_arr[i] = new_arr[i][1] - temp[0] + new_arr[i][1] + new_arr[i][0]
        heappush(heap, temp)
        heappush(heap,new_arr[i])

    # second iter
    new_arr_2 = [0] * n
    minus = n
    for i in range(n):
        new_arr_2[i] = (-new_maxi_arr[i]+minus, new_maxi_arr[i]) 
        minus -= 1

    # print(new_arr_2)
    new_maxi_arr = [0] * n
    heap = [new_arr_2[1]]
    for i in range(2, n):
        temp = heappop(heap)
        new_maxi_arr[i] = arr[i] - temp[0] + new_arr_2[i][1] + new_arr_2[i][0]
        heappush(heap, temp)
        heappush(heap,new_arr_2[i])
    
    print(max(new_maxi_arr))
    
    # print(new_maxi_arr)

for t in range(int(input())):
    solve()