from math import prod
from collections import defaultdict

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda:0)
    for num in arr:
        i = 2
        while i*i <= num:
            while num % i == 0:
                num = num // i
                dict[i] += 1
            i += 1
        if num != 1:
            dict[num] += 1
    rare_count = 0
    count = 0
    # print(dict)
    for i, value in dict.items():
        count += value // 2
        if value % 2 == 1:
            rare_count += 1
    print(count + rare_count // 3)
