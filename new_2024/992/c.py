import sys
input = sys.stdin.readline

def bigger(pow, k):
    pow = max(0, pow)
    i = 0
    while i <= pow:
        if 2 ** i >= k:
            return True
        i += 1
    return False
def solve():
    n, k = map(int, input().split())
    temp_k = k
    front = []
    end = []
    last = 1
    while last <= n:
        powe = max(0, n - last - 1)
        if last == n and temp_k == 1:
            front.append(last)
            temp_k = 0
            break
        if bigger(powe, temp_k):
            front.append(last)
        else:
            temp_k = temp_k - 2 ** powe
            end.append(last)
        last += 1
        # print(temp_k)
    # print(temp_k)
    if temp_k > 0:
        print(-1)
    else:
        print(*front, *end[::-1])



    
for t in range(int(input())):
    solve()