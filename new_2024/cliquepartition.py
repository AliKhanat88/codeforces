from itertools import permutations

def check_ok(arr, k):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(i - j) + abs(arr[i] - arr[j]) > k:
                return False
    return True

def check(i, j, k):
    left = i + (j - i + 1) // 2
    ans = [l for l in range(i, left)][::-1] + [l for l in range(j, left-1, -1)]
    if check_ok(ans, k):
        return True, ans
    else:
        return False, []

def solve():
    n, k = map(int, input().split())
    if k == 1:
        print(*[i for i in range(1, n+1)])
        print(n)
        print(*[i for i in range(1, n+1)])
        return
    i = 1
    q = 0
    ans = []
    ans_c = []
    # print(check(1, n, k))
    while i <= n:
        if i == n:
            ans.append(n)
            q += 1
            ans_c.append(q)
            break
        # print(i)
        for j in range(n, i, -1):
            can, temp_ans = check(i, j, k)
            if can:
                q += 1
                for x in temp_ans:
                    ans.append(x)
                    ans_c.append(q)
                i = j + 1
                break
            else:
                j -= 1
    print(*ans)
    print(q)
    print(*ans_c) 

for t in range(int(input())):
    solve()


def brute(n, k):
    arr = [i for i in range(1, n+1)]
    perms = list(permutations(arr))

    for perm in perms:
        if check_ok(perm, k):
            print(perm)
    

# brute(5, 4)