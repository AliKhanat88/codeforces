from bisect import bisect_right
def solve():
    s = input()

    graph = [[] for i in range(len(s)+2)]
    cur = 0
    graph[0].append(-1)
    for i in range(len(s)):
        if s[i] == "(":
            cur += 1
        else:
            cur -= 1
        graph[cur].append(i)
    
    # print(graph)
    cur = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "(":
            cur += 1
        else:
            cur -= 1

        temp = bisect_right(graph[cur * 2 + 1], i)
        if temp >= len(graph[cur * 2 + 1]):
            upper = len(s)+1
        else:
            upper = graph[cur * 2 + 1][temp]
        # print(cur * 2 + 1, upper, i)
        ans += bisect_right(graph[cur], upper) - bisect_right(graph[cur], i)
    print(ans)




for t in range(int(input())):
    solve()