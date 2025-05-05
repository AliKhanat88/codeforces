import sys
input = sys.stdin.readline

def q1(i):
    print("?", 1, i+1, flush=True)
    return input().strip()

def q2(l, r):
    print("?", 2, l+1 ,r+1, flush=True)
    return int(input())

def solve():
    n = int(input())
    temp = q1(0)
    dis = [0]
    ans = [temp]

    def bin(x):
        l = 0
        r = len(dis) - 1
        while r - l > 1:
            m = (r + l) // 2 
            temp = q2(dis[m], x)
            if temp == len(dis) - m + 1:
                r = m - 1
            else:
                l = m

        if q2(dis[r], x) < len(dis) - r + 1:
            return r
        if q2(dis[l], x) < len(dis) - l + 1:
            return l
        return -1
    

    for i in range(1, n):
        temp = bin(i)
        if temp == -1:
            ans.append(q1(i))
            dis.append(i)
        else:
            ans.append(ans[dis[temp]])
            dis.pop(temp)
            dis.append(i)

    print("!", "".join(ans))
    
    




solve()