from bisect import bisect_left

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    bin_arr = []

    for i in range(1, n):
        bin_arr.append((n - i - arr[i] ,i))
    
    bin_arr.sort()

    stack = []
    visited = set()
    for i in range(len(bin_arr)):
        if bin_arr[i][0] == 0:
            stack.append((bin_arr[i][0], bin_arr[i][1], 0))
        elif bin_arr[i][0] > 0:
            break
    # print(bin_arr)
    maxi = n
    while stack:
        # print(stack)
        cur = stack.pop()
        visited.add(cur[1])
        maxi = max(maxi, n + abs(cur[2]) + cur[1])
        new = cur[2] - cur[1]
        temp_ind = bisect_left(bin_arr, (cur[2] - cur[1], -1))
        while temp_ind < len(bin_arr):
            if bin_arr[temp_ind][0] == new:
                if bin_arr[temp_ind][1] not in visited:
                    stack.append((bin_arr[temp_ind][0],  bin_arr[temp_ind][1], new))
            else:
                break
            temp_ind += 1
        
    print(maxi)


for t in range(int(input())):
    solve()