from heapq import heappop, heappush
def solve():
    q = int(input())
    arr = [-1] * (q+1)
    heapi = []
    index = 0
    read_index = 0
    for i in range(q):
        ip = [*map(int, input().split())]
        if ip[0] == 1:
            arr[index] = ip[1]
            heappush(heapi, (-ip[1], index))
            index += 1
        elif ip[0] == 2:
            while arr[read_index] == -1:
                read_index += 1
            print(read_index+1, end=" ")
            arr[read_index] = -1
            read_index += 1
        else:
            temp = heappop(heapi)
            while arr[temp[1]] == -1:
                temp = heappop(heapi)
            print(temp[1]+1, end=" ")
            arr[temp[1]] = -1
        # print(arr)
        # print(heapi)
    print()
solve()