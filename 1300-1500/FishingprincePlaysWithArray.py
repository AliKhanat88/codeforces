from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))

    dict_a = defaultdict(lambda:0)
    for i, num in enumerate(a):
        temp = num
        times = 1
        while temp % m == 0:
            temp = temp // m
            times = times * m
        dict_a[i] = [temp, times]
    
    dict_b = defaultdict(lambda:[])
    for i, num in enumerate(b):
        temp = num
        times = 1
        while temp % m == 0:
            temp = temp // m
            times = times * m
        dict_b[i] = [temp, times]
    # print(dict_a)
    # print(dict_b)
    # print("After")
    j = 0
    i = 0
    while i < k and j < n:
            while True:
                if j >= n:
                    break
                if dict_b[i][0] == dict_a[j][0]:
                    if dict_b[i][1] > dict_a[j][1]:
                        dict_b[i][1] -= dict_a[j][1]
                        dict_a[j][1] = 0
                        j += 1
                    elif dict_b[i][1] < dict_a[j][1]:
                        dict_a[j][1] -= dict_b[i][1]
                        dict_b[i][1] = 0
                        i += 1
                        break
                    else:
                        dict_b[i][1] = 0
                        dict_a[j][1] = 0
                        j += 1
                        i += 1
                        break
                else:
                    # print(dict_a)
                    # print(dict_b)
                    print("NO")
                    return
            
    if i >= k and j >= n:
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    solve()
