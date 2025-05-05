from math import log2

def solve():
    n = int(input())
    
    num = int(log2(n))
    ans = []
    if 2 ** num == n:
        ans = [1, 3, 2 ** num - 2, 2 ** num - 1, 2 ** num]
    elif n % 2 == 1:
        ans = [1, 3, n -1 , n]
    else:
        ans = [2 ** num, 2 ** num + 1, 2 ** num - 1]
    
    # print(ans, "ans")
    temp_ans = []
    for i in range(1, n + 1):
        if i not in ans:
            temp_ans.append(i)
    # print(temp_ans, "temp_ans")
    ans = temp_ans + ans
    # print(ans)
    ans_num = 0
    for i in range(n):
        if i % 2 == 0:
            ans_num = ans_num & ans[i]
        else:
            ans_num = ans_num | ans[i]
    print(ans_num)
    print(*ans)
    


for t in range(int(input())):
    solve()