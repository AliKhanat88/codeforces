def find_min(healths, powers, k, n):
    mini = 9999999999
    mini_mon = -1
    for i in range(n):
        if powers[i] < mini and healths[i] - k > 0:
            mini_mon = healths[i]
            mini = powers[i]
    return mini, mini_mon


def all_kill(n, k, healths, powers):
    max_health = max(healths) - k
    temp = k
    next_min, next_mini_mon = find_min(healths, powers, temp, n)
    is_doable = False
    while True:
        if max_health <= 0:
            is_doable = True
            break
        k = k - next_min
        temp = temp + k 
        if  k <= 0:
            break
        max_health = max_health - k
        if next_mini_mon - temp <= 0:
            next_min, next_mini_mon = find_min(healths, powers, temp, n)
        
    if is_doable:
        print("Yes")
    else:
        print("No")


def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        healths = list(map(int, input().split()))
        powers = list(map(int, input().split()))
        all_kill(n, k, healths, powers)

main()