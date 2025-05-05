def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print("TEST")
    stack = [(arr[0], 1)]
    for i in range(1,n):
        # print(stack)
        temp_sum = arr[i]
        temp_count = 1
        while len(stack) > 0 and stack[-1][0] >= temp_sum // temp_count:
            temp = stack.pop()
            temp_sum += temp[0] * temp[1]
            temp_count += temp[1]
        if temp_count - temp_sum % temp_count > 0:
            stack.append((temp_sum // temp_count, temp_count - temp_sum % temp_count))
        if temp_sum % temp_count > 0:
            stack.append((temp_sum // temp_count + 1, temp_sum % temp_count))
        # print(stack)
    print(stack[-1][0] - stack[0][0])
for t in range(int(input())):
    solve()