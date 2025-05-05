import sys
input = sys.stdin.readline

def find_msb(x):
    for i in range(61, -1, -1):
        if x & (2 ** i) != 0:
            return i
        
def solve():
    x, m = map(int, input().split())
    m_msb = find_msb(m)
    x_msb = find_msb(x)
    count = 0
    mini = min(m, 2 ** (x_msb + 1))
    for i in range(1, mini + 1):
        if (i ^ x) % x == 0 or (i ^ x) % i == 0:
            count += 1
    if m <= mini:
        print(count)
        return
    # print(mini, count, "mini, count")
    # print(m_msb, x_msb, "msb of m and x")
    
    maxi = 0
    for i in range(m_msb, x_msb + 1, -1):
        if (2 ** i) & m != 0:
            maxi += (2 ** i)
    # print(maxi, "maxi")
    if maxi > mini:
        count = count + (maxi // x - mini // x)
    last = max(mini, maxi)
    for i in range(last + 1, m+1):
        if (i ^ x) % x == 0 or (i ^ x) % i == 0:
            count += 1
    print(count)


for t in range(int(input())):
    solve()