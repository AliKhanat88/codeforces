import sys
input = sys.stdin.readline

def print_poss(n, w, h, cakes, shooters):
    step_poss = 2 * w - 2 * h
    mini = maxi = cakes[0] - shooters[0]
    for i in range(1, n):
        temp_diff = cakes[i] - shooters[i]
        mini = min(mini, temp_diff)
        maxi = max(maxi, temp_diff)
        if maxi - mini > step_poss:
            print("NO")
            return
    print("YES")
            

for t in range(int(input())):
    n, w, h = map(int, input().split())
    cakes = list(map(int, input().split()))
    shooters = list(map(int, input().split()))
    print_poss(n, w, h, cakes, shooters)