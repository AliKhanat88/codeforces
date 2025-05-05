f = open("output.txt", "w")

def solve(t):
    n, k = map(int, input().split())
    mini = 99999999999999999999999999
    for i in range(n):
        mini = min(mini, int(input()))
    
    if mini * max(0, (n - 2)) * 2 + mini <= k:
        f.write(f"Case #{t}: YES\n")
    else:
        f.write(f"Case #{t}: NO\n")

for t in range(int(input())):
    solve(t+1)