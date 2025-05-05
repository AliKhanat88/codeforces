import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0] * n

    for i in range(n):
        arr[i] = [*map(int, input().split())]
    
    i = 0 
    while i < n:
        j = i + 1
        while j < n:
            count = 0
            for k in range(5):
                if arr[i][k] < arr[j][k]:
                    count += 1
            if count < 3:
                break
            j += 1
        if j >= n:
            break
        i = j
    # print(i)
    for j in range(n):
        if i != j:
            count = 0
            for k in range(5):
                if arr[i][k] < arr[j][k]:
                    count += 1
            if count < 3:
                print(-1)
                return
    print(i+1)

        
for t in range(int(input())):
    solve()