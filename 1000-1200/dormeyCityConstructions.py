from math import ceil
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    i = 0
    k = n -1
    while i < k and arr[i] != arr[k]:
        i += 1
        k -= 1
    # print(i)
    if i == 0:
        print(n // 2)
        return
    elif i >= k:
        count = n - 1
        rem = 0
    else:
        count = i * 2
        rem = n - count - 1
    pairs = count + 1
    comb = ceil((pairs-3) / 2)
    comb1 = ceil((pairs-4) / 2)
    if comb == comb1:
        count += comb * (comb+1)
    else:
        count += comb 
        count += comb1 * (comb1 + 1)
    count += pairs // 2 * rem 
    print(count)

for t in range(int(input())):
    solve()