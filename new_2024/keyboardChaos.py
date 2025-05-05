from collections import defaultdict

def solve():
    n, e = map(int, input().split())
    arr = [0] * n
    dict = defaultdict(lambda: False)
    for i in range(n):
        arr[i] = list(input())[::-1]
        if len(set(arr[i])) == 1:
            dict[arr[i][0]] = True
    
    mini = float("inf")
    ans = ["N", "O"]
    for temp in range(ord("a"), ord("a") + e):
        char = chr(temp)
        if dict[char] == False:
            new_ans = []
            for i in range(n):
                j = len(arr[i]) -1
                while j >= 0:
                    if arr[i][j] == char:
                        new_ans.append(char)
                    else:
                        break
                    j -= 1
            new_ans.append(char)
            if mini > len(new_ans):
                mini = len(new_ans)
                ans = new_ans
    print("".join(ans))


# for t in range(int(input())):
solve()