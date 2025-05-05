def print_components(n, arr):
    dict = {}
    for i in range(n):
        dict[arr[i]] = i
    count = 0
    start = n-1
    great_mini = 9999999999
    for i in range(n, 0, -1):
        can_add = True
        mini = i
        if start >= dict[i]:
            while start >= 0 and arr[start] != i:
                mini = min(arr[start], mini)
                if arr[start] >= great_mini:
                    can_add = False
                start -= 1
            if arr[start] >= great_mini:
                can_add = False
            if can_add == True:
                count += 1
            start -= 1
        great_mini = min(mini, great_mini)
    print(count)

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_components(n, arr)