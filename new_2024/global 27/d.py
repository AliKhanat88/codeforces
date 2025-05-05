from copy import deepcopy
def bigger(a, b):
    a = deepcopy(a)
    b = deepcopy(b)
    if a[1] >= b[1]:
        while a[1] > b[1]:
            if a[0] > b[0]:
                return True
            a[1] -= 1
            a[0] *= 2
        if a[0]>= b[0]:
            return True
        else:
            return False
    else:
        while a[1] < b[1]:
            if a[0] < b[0]:
                return False
            b[1] -= 1
            b[0] *= 2
        if a[0] >= b[0]:
            return True
        else:
            return False

            
            
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    # sumi_arr = [0] * (n + 1)

    # for i in range(1, n+1):
    #     sumi_arr[i] = sumi_arr[i-1] + arr[i-1]
    
    # print(sumi_arr)
    
    for i in range(n):
        num = [arr[i], 0]
        while num[0] % 2 == 0:
            num[0] //= 2
            num[1] += 1
        arr[i] = num
    # print(arr)
    stack = []
    sumi = 0
    ans = []
    for i in range(n):
        while len(stack) > 0:
            temp = stack[-1]
            temp_check = [arr[i][0], arr[i][1] + temp[1]]
            # print(temp)
            if bigger(temp_check, temp):
                stack.pop(-1)
                # print(temp)
                arr[i][1] += temp[1]
                temp_p = pow(2, temp[1], MOD)
                sumi = (sumi - (temp_p * temp[0]) + temp[0]) % MOD
            else:
                break
            # print(stack)
        stack.append(arr[i])
        sumi = (sumi + (arr[i][0] * pow(2, arr[i][1], MOD))) % MOD
        # print(stack, arr[i])
        ans.append(sumi)
    print(*ans)



for t in range(int(input())):
    solve()