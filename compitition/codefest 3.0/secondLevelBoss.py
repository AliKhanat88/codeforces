n = int(input())
arr = list(set(map(int, input().split())))
arr.sort(reverse=True)
if len(arr) == 1:
    print("NO")
else:
    print(arr[1])
