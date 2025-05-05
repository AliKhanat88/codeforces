
def check(arr, arr_m, last):
    arr = arr[:]

    dict_index = {}

    cur = 0
    for i in range(last+1):
        if arr[i] != 0:
            if dict_index.get(arr[i], None) != None:
                arr[dict_index[arr[i]]] = 0
            dict_index[arr[i]] = i
    
    for i in range(last+1):
        if arr[i] == 0:
            cur += 1
        else:
            if cur < arr_m[arr[i]-1]:
                return False
            else:
                cur = cur - arr_m[arr[i]-1]
    return True

def solve():
    n, m = map(int, input().split())

    seti = set()
    arr = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    
    i = 0
    while i < n:
        if arr[i] != 0:
            seti.add(arr[i])
            if len(seti) >= m:
                break
        i += 1
    # print("TEST")
    # print(temp_arr)
    # print(arr)
    # print(arr_m)

    # print(check(arr, arr_m, 2))
    # print(check(arr, arr_m, 2))
    if i >= n:
        print(-1)
        return
    lower = i
    upper = n - 1
    while upper - lower > 1:
        mid = lower + (upper - lower) // 2
        # print(lower,upper, mid)
        temp = check(arr, arr_m, mid)
        if temp:
            upper = mid
        else:
            lower = mid + 1
    # print(lower, upper)
    if check(arr, arr_m, lower):
        print(lower+1)
    elif check(arr,arr_m, upper):
        print(upper+1)
    else:
        print(-1)
        return

            

# for t in range(int(input())):
solve()