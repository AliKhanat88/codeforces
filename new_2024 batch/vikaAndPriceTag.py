def findOp(a, b):
    count = 0
    while b != 0:
        if a < b:
            count += 1
            a, b = b, b - a
        else:
            temp = a // b
            count += (temp + temp // 2)
            
            if temp % 2 == 0 and a % b == 0:
                count -= 1
            if temp % 2 == 0 and a % b != 0:
                a, b = (a % b), b
            else:
                a, b = b , (a % b)
            # print(temp, count, a, b)
    return count

# print(findOp(9, 14))
def solve():
    n = int(input())
    
    a = list(map(int ,input().split()))
    b = list(map(int, input().split()))

    j = 0
    while j < n:
        if a[j] != 0 or b[j] != 0:
            per = findOp(a[j], b[j])
            break
        j += 1
    if j >= n:
        print("YES")
        return
    # print(per, j)
    for i in range(j+1, n):
        if a[i] == 0 and b[i] == 0:
            continue
        temp = findOp(a[i], b[i])
        if (max(per, temp) - min(per, temp)) % 3 == 0:
            per = max(temp, per)
        else:
            # print(per, temp, i)
            print("NO")
            return
        # print(per, temp, i)
    print("YES")


for t in range(int(input())):
    solve()