def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    mini = k
    temp = 1
    if k == 4:
        count = 0
        s2 = 0
        for num in arr:
            if num % k == 0:
                print(0)
                return
            else:
                mini = min(mini, k - num % k)
            if num in (2, 6, 10):
                s2 += 1
            if num in (1, 5, 9):
                count += 1
        if s2 >= 2:
            print(0)
            return 
        elif s2 == 1 and count >= 1:
            print(min(mini, 1))
            return 
        elif s2 == 0 and count >= 2:
            print(min(mini, 2))
            return
        else:
            print(mini)
    else:
        for num in arr:
            if num % k == 0:
                print(0)
                return
            else:
                mini = min(mini, k - num % k)
            
        print(mini)


for t in range(int(input())):
    solve()