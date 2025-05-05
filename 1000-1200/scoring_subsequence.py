def print_sub(n, arr):
    r = "1 "
    per = 0
    per_score = 1
    for i in range(1, n):
        if arr[per] / (per_score + 1) < 1:
            r += f"{per_score} "
            per = per + 1
        else:
            per_score += 1
            r += f"{per_score} "
    print(r)
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print_sub(n, arr)