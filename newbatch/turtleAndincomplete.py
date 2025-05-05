def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    # print("TES")
    # print(arr)
    temp = set(arr)
    if len(temp) == 1:
        temp = [*temp][0]
        if temp == -1:
            is2 = False
            for i in range(n):
                if is2:
                    arr[i] = 2
                else:
                    arr[i] = 1
                is2 = not is2
            print(*arr)
            return

    per = None
    for i in range(n):
        if arr[i] != -1 and per == None:
            per = i
        elif arr[i] != -1:
            temp = i
            while temp - per > 1:
                if arr[temp] == arr[per] and arr[temp] == 1:
                    arr[per+1] = 2
                    per += 1
                elif arr[temp] > arr[per]:
                    arr[temp-1] = arr[temp] // 2
                    temp -= 1
                elif arr[per] >= arr[temp]:
                    arr[per+1] = arr[per] // 2
                    per += 1 
            if max(arr[per], arr[temp]) // 2 != min(arr[per], arr[temp]):
                print(-1)
                return
            per = i
    
    # print(arr)
    for i in range(n):
        if arr[i] != -1:
            j = i
            while j >= 1:
                if arr[j] > 1:
                    arr[j-1] = arr[j] // 2
                else:
                    arr[j-1] = arr[j] * 2
                j -= 1
            break
    for i in range(n-1, -1, -1):
        if arr[i] != -1:
            j = i
            while j < len(arr) - 1:
                if arr[j] > 1:
                    arr[j+1] = arr[j] // 2
                else:
                    arr[j+1] = arr[j] * 2
                j += 1
            break
    print(*arr)
for t in range(int(input())):
    solve()