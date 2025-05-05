import sys

input = sys.stdin.readline

from collections import defaultdict
maxi = 100
divisors = [[1] for i in range(maxi+1)]

for i in range(2, maxi+1):
    for j in range(i, maxi+1, i):
        divisors[j].append(i)

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    after_arr = defaultdict(lambda: 0)
    arr.sort()
    nums = set()
    divs = defaultdict(lambda: [])
    for i in range(n):
        after_arr[arr[i]] = n - i -1
        for div in divisors[arr[i]]:
            nums.add(div)
            divs[div].append(arr[i])
    print(divs)
    print(nums)
    ans = 0
    for div in nums:
        dict = defaultdict(lambda: 0)
        total_sum = 0
        for arr_num in divs[div]:
            count = 0
            for divisor_num in divisors[arr_num][1:]:
                count += dict[divisor_num]
            ans += ((total_sum - count) * after_arr[arr_num] * div)
            dict[arr_num // div] += 1
            total_sum += 1
    print(ans)

    
    print()


for t in range(int(input())):
    solve()
