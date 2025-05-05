import sys
input = sys.stdin.readline



def solve():
    n, m, q = map(int, input().split())
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, input().split()))
    

    def less(l, r, x, col):
        while l + 1 < r:
            mid = (l + r) // 2
            if data[mid][col] < x:
                l = mid
            if data[mid][col] >= x:
                r = mid - 1
        if data[r][col] < x:
            return r
        if data[l][col] < x:
            return l
        return -1
    
    def greater(l, r, x, col):
        while l + 1 < r:
            mid = (l + r) // 2
            if data[mid][col] > x:
                r = mid
            if data[mid][col] <= x:
                l = mid + 1
        if data[l][col] > x:
            return l
        if data[r][col] > x:
            return r
        return -1
    

    # print(data)

    for i in range(m):
        for j in range(1, n):
            data[j][i] = data[j][i] | data[j-1][i]
            
    # print(data)
    
    for i in range(q):
        temp_m = int(input())
        # print(temp_m)
        # print("start")
        l, r = 0, n - 1
        done = False
        for j in range(temp_m):
            temp = input().strip().split()
            # print(l ,r, j)
            if done != True:
                col, x = int(temp[0]) - 1, int(temp[2])
                if temp[1] == ">":
                    l = greater(l, r, x, col)
                    if l == -1:
                        # print(-1)
                        done = True
                else:
                    r = less(l, r, x, col)
                    if r == -1:
                        # print(-1)
                        done = True
        if done:
            print(-1)
        else:
            print(l+1)


solve()