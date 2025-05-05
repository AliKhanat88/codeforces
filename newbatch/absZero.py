m = 40
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    moves = []
    while len(moves) < m:
        maxi = max(arr)
        sec_max = min(arr)
        if (maxi - sec_max) % 2 != 0:
            print(-1)
            return
        oper = sec_max + (maxi - sec_max) // 2
        for i in range(n):
            arr[i] = abs(arr[i] - oper)
        moves.append(oper)
    
    if max(arr) != 0 and min(arr) != 0:
        print(-1)
        return
    # if arr[0] != 0:
    #     moves.append(arr[0])
    # if len(moves) > m:
    #     print(-1)
    #     return
    print(len(moves))
    print(*moves)

for t in range(int(input())):
    solve()