for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2 == 0:
        print(-1)
    else:
        ans = [-1] * n
        left = n // 2
        right = n // 2
        ans[left] = 1
        left -= 1
        right += 1
        left_ans = 3
        right_ans = 2
        for i in range(n // 2):
            ans[right] = right_ans
            ans[left] = left_ans
            left -= 1
            right += 1
            left_ans += 2
            right_ans += 2
        print(*ans)