def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(1)
        return
    
    count = 0

    for i in range(1, n):
        if arr[i] == 0:
            if arr[i-1] == -1:
                continue
            elif arr[i-1] == 0:
                arr[i-1] = -1
                count += 1
            else:
                j = i - 1
                minusOneFound = False
                twoFound = False
                while j > -1:
                    if arr[j] == -1:
                        minusOneFound = True
                        break
                    elif arr[j] == 0:
                        break
                    elif arr[j] == 2:
                        twoFound = True

                    j -= 1
                if j == -1 and arr[0] != 0:
                    minusOneFound = True
                if twoFound:
                    count += 1
                    arr[i] = -1
                else:
                    count += 1
                    if minusOneFound:
                        arr[i] = -1
            
        # print(count, arr)
    if arr[-1] != -1:
        count += 1
    # print(arr)
    print(count)


# for t in range(int(input())):
solve()