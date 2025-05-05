from collections import defaultdict

def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    dict1 = defaultdict(lambda:0)
    dict2 = defaultdict(lambda:0)
    dict3 = defaultdict(lambda:0)
    dict4 = defaultdict(lambda:0)
    for i in range(2, n):
        dict1[(arr[i-2], arr[i-1])] += 1
        dict2[(arr[i-1], arr[i])] += 1
        dict3[(arr[i-2], arr[i])] += 1
        dict4[(arr[i-2], arr[i-1], arr[i])] += 1
    sumi = 0
    for key, val in dict1.items():
        if dict1[key] > 1:
            sumi += ((dict1[key] - 1) * (dict1[key])) // 2

    
    for key, val in dict2.items():
        if dict2[key] > 1:
            sumi += ((dict2[key] - 1) * (dict2[key])) // 2

    
    for key, val in dict3.items():
        if dict3[key] > 1:
            sumi += ((dict3[key] - 1) * (dict3[key])) // 2

    
    for key, val in dict4.items():
        if dict4[key] > 1:
            sumi = sumi - 3 * ((dict4[key] - 1) * (dict4[key])) // 2
    # print(dict1)
    # print(dict2)
    # print(dict3)
    # print(dict4)
    print(sumi)

for t in range(int(input())):
    solve()