def recur(stack, b, ans_or, brr, x):
    if b < 0:
        return -5
    temp_ans = -5
    while ans_or > x and b >= 0:
        if brr[b] % 2 == 1 or brr[b] == 0:
            b -= 1
            continue
        if ans_or - (2 ** b) <= x:
            temp_ans = recur(stack[:], b - 1, ans_or, brr, x)
        new_stack = []
        odd = False
        for i in range(len(stack)):
            count = 0
            for j in range(len(stack[i])):
                if stack[i][j] & (2 ** b) != 0:
                    count += 1
            if count % 2 == 1 and odd == True:
                odd = False
                for j in range(len(stack[i])):
                    new_stack[-1].append(stack[i][j])
            elif count % 2 == 1 and odd == False:
                odd = True
                new_stack.append(stack[i][:])
            elif count % 2 == 0 and odd == False:
                new_stack.append(stack[i][:])
            elif count % 2 == 0 and odd == True:
                for j in range(len(stack[i])):
                    new_stack[-1].append(stack[i][j])
        stack = new_stack
        new_ans_or = 0
        for i in range(len(stack)):
            temp = 0
            for j in range(len(stack[i])):
                temp = temp ^ stack[i][j]
            new_ans_or = new_ans_or | temp
        ans_or = new_ans_or
        b -= 1
    # print(stack, ans_or, temp_ans)
    if ans_or <= x:
        return max(len(stack), temp_ans)
    return temp_ans

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    temp = 0
    ans_or = 0
    stack = []
    brr = [0] * 30
    for i in range(n):
        temp = temp ^ arr[i]
        for b in range(30):
            if arr[i] & (2 ** b) != 0:
                brr[b] += 1
        stack.append([arr[i]])
        ans_or = ans_or | arr[i]
    if temp > x:
        print(-1)
        return
    
    # print(stack)
    # print(ans_or)
    # print(0)
    b = 29
    print(recur(stack, b, ans_or, brr, x))

    
    

for t in range(int(input())):
    solve()