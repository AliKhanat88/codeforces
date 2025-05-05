def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    visited = [-1] * (n+2)

    done = False

    cur = 1
    
    ans = 0

    for i in range(1, n+1):
        if visited[i] == -1:
            length = 1
            visited[i] = cur
            j = arr[i-1]
            while j != i:
                if done == False and (visited[j-1] == cur or visited[j+1] == cur):
                    ans -= 1
                    done = True
                visited[j] = cur
                j = arr[j-1]
                length += 1
            ans = ans + length - 1
            cur += 1
    if done == False:
        ans += 1
    print(ans)

    
for t in range(int(input())):
    solve()