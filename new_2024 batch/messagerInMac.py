from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def check(n,l,x,arr):

    for i in range(x-1, n):
        # print("in it")
        heap2 = []
        cur_sum = 0
        for j in range(i, i-x, -1):
            cur_sum += arr[j][0]
            heappush(heap2, -arr[j][0])
        
        if cur_sum + arr[i][1] - arr[i-x+1][1] <= l:
            # print(cur_sum, i, i-x-1)
            return True
        # print(cur_sum, heap2)
        for j in range(i-x, -1, -1):
            if abs(heap2[0]) > arr[j][0]:
                temp = heappop(heap2)
                cur_sum += temp
                heappush(heap2, -arr[j][0])
                cur_sum += arr[j][0]
            if cur_sum + arr[i][1] - arr[j][1] <= l:
                return True
            # print(cur_sum, heap2)
    return False


def solve():
    n, l = map(int, input().split())  
    arr = [0] * n
    for i in range(n):
        arr[i] = tuple(map(int, input().split()))
    
    arr.sort(key=lambda x:x[1])

    # print("TEST")
    # print(arr)
    # print(prefix_sum)
    lower = 0
    upper = n
    while upper - lower > 1:
        mid = lower + (upper - lower) // 2
        if check(n,l,mid,arr):
            lower = mid 
        else:
            upper = mid - 1
    if check(n,l,upper,arr):
        print(upper)
    else:
        print(lower)
    # print(check(n,l,3, arr))

    # print(0)
    


for t in range(int(input())):
    solve()  


