def solve():
    n = int(input())
    tree = [[] for i in  range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    s = list(input())
    # print(s)
    count_0 = 0
    count_1 = 0
    stack = [1]
    visited = [False] * (n + 1)
    leaves = []
    while len(stack) != 0:
        cur = stack.pop()
        visited[cur] = True
        done = False
        for child in tree[cur]:
            if visited[child] == False:
                done = True
                stack.append(child)
        if done == False:
            if s[cur-1] == "1":
                count_1 += 1
            elif s[cur-1] == "0":
                count_0 += 1
            else:
                leaves.append(cur)


    turn = 1
    ans = 0
    if s[0] == "?":
        # print("Hell")
        if count_0 > count_1:
            s[0] = "1"
            ans = count_0
            turn = turn ^ 1
        elif count_1 > count_0:
            s[0] = "0"
            ans = count_1
            turn = turn ^ 1
        else:
            temp = s.count("?")
            ans = count_0
            if (temp - len(leaves)) % 2 == 1:
                turn = turn ^ 1

    else:
        if s[0] == "0":
            ans += count_1
        else:
            ans += count_0

    
    # print(turn, "turn", s[0])
    for leave in leaves:
        if s[leave-1] == "?":
            if turn == 1:
                ans += 1
            # print(turn, leave)
            turn = turn ^ 1
            
    # print(s)
    # print(leaves)
    print(ans)



for t in range(int(input())):
    solve()