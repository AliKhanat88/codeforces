def solve(n, m , arr):
    count_1 = 0
    count_2 = 0
    ls = set()
    for num in arr:
        if num == -1:
            count_1 += 1
        elif num == -2:
            count_2 += 1
        elif num <= m:
            ls.add(num)
    ls = list(ls)
    ls.sort()
    maxi = 0
    for i, num in enumerate(ls):
        temp = len(ls)
        left = i + 1
        right = len(ls) - i - 1
        if count_1 > num - left:
            temp += num-left
        else:
            temp += count_1
        if m - right - num > count_2:
            temp += count_2
        else:
            temp += m - right - num
        if temp > maxi:
            maxi = temp
    temp = min(m, count_1+len(ls))
    if temp > maxi:
        maxi = temp
    temp = min(m, count_2+len(ls))
    if temp > maxi:
        maxi = temp
    print(maxi)
        
    



for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(n, m , arr)