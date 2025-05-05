def find_diff(x):
    if x == 0:
        return 0
    mini = 10
    maxi = -1
    while x > 0:
        temp = x % 10
        maxi = max(maxi, temp)
        mini = min(mini, temp)
        x = x // 10
        # print(maxi, mini)
    return maxi - mini

def solve():
    a, b = input().split()
    a = (len(b) - len(a)) * "0" + a
    mini_ans = 10
    ans = None
    start = None
    for i in range(len(b)):
        if a[i] != b[i]:
            c = b
            d = a
            for j in range(int(a[i])+1,int(b[i])):
                temp = int(b[:i] + f"{j}" * (len(b) - i))
                if find_diff(temp) < mini_ans:
                    ans = temp
                    mini_ans = find_diff(temp)
            start = i+1
            break
    if start == None:
        print(a)
        return
    for i in range(start, len(b)):
        for j in range(int(c[i])-1, -1, -1):
            temp = int(c[:i] + f"{j}" * (len(b) - i))
            if find_diff(temp) < mini_ans:
                ans = temp
                mini_ans = find_diff(temp)
    for i in range(start, len(b)):
        for j in range(int(d[i])+1, 10, 1):
            temp = int(d[:i] + f"{j}" * (len(b) - i))
            if find_diff(temp) < mini_ans:
                ans = temp
                mini_ans = find_diff(temp)
    if find_diff(int(a)) < mini_ans:
        ans = int(a)
        mini_ans = find_diff(int(a))
    if find_diff(int(b)) < mini_ans:
        ans = int(b)
        mini_ans = find_diff(int(b))
    print(ans)



for t in range(int(input())):
    solve()