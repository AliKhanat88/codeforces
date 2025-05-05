def solve():
    n, k = map(int, input().split())

    if k == 1:
        print(25)
        print(3, end=" ")
        i = 1
        while i < 25:
            print(2 ** i, end= " ")
            i += 1
        print()
    else:
        ans = [0] * 25
        i = 0 
        while sum(ans[:i]) + 2 ** i < k:
            ans[i] = 2 ** i
            i += 1
        assert k - sum(ans[:i]) - 1 >= 0
        ans[i] = k - sum(ans[:i]) - 1
        i += 1
        temp_k = i
        start = sum(ans[:i]) + 2
        while i < 25:
            ans[i] = start 
            i += 1
            start = sum(ans[:i]) + 1
        ans[-1] = ans[temp_k+1] + k
        print(25)
        print(*ans)

        
    
for t in range(int(input())):
    solve()