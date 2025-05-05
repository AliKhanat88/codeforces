from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    start = 0
    isAlice = True
    while start <= n + 1:
        if isAlice:
            while c[start] > 1:
                start += 1
            if c[start] == 0:
                print(start)
                return 
            c[start] -= 1
            start += 1
            isAlice = not isAlice
        else:   
            while c[start] > 1:
                start += 1
            print(start)
            return

for i in range(int(input())):
    solve()