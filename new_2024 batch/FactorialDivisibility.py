from collections import Counter

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    a_mini = min(arr)
    c = Counter(arr)
    while a_mini < x:
        if c[a_mini] % (a_mini+1) == 0:
            c[a_mini+1] = c[a_mini+1] + c[a_mini] // (a_mini+1)
            a_mini += 1
        else:
            print("No")
            exit()
    
    print("Yes")

solve()


