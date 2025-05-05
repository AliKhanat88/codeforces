from collections import defaultdict

def solve():
    n = int(input())
    a = input().split()
    b = input().split()
    total = 0
    dict = defaultdict(lambda:0)
    for i in range(n):
        dict[a[i]] += 1
        dict[b[i]] -= 1

    arr = [dict[f"{num}"] for num in range(10)]
    for key, val in dict.items():
        if int(key) > 9:
            arr[len(key)] += val
            total += abs(val)
    
    for i in range(9, 1, -1):
        if arr[1] < 0:
            if arr[i] > 0:
                if abs(arr[1]) > arr[i]:
                    total += abs(arr[i])
                    arr[1] = arr[1] + arr[i]
                    arr[i] = 0
                    
                else:
                    total += abs(arr[1])
                    
                    arr[i] = arr[i] + arr[1]
                    arr[1] = 0
                    break
        elif arr[1] > 0:
            if arr[i] < 0:
                if abs(arr[i]) >= arr[1]:
                    total += abs(arr[1])
                    arr[i] = arr[1] + arr[i]
                    arr[1] = 0
                    
                    break
                else:
                    total += abs(arr[i])
                    
                    arr[1] = arr[i] + arr[1]
                    arr[i] = 0
                    
    for num in arr:
        total += abs(num)
    print(total)


for t in range(int(input())):
    solve()



