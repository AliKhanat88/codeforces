def solve(n, arr):
    if n == 1:
        for i in range(1, arr[0]+1):
            if arr[0] % i == 0:
                print(arr[0] // i, end=" ")
            else:
                print(arr[0] // i + 1, end=" ")
        print()
        return
    increasing = True
    maxi = max(arr)
    parts = []
    per = 0
    i = 1
    while i < n:
        if increasing:
            if arr[i] < arr[i-1]:
                increasing = not increasing
            else:
                i += 1
        else:
            if arr[i] > arr[i-1]:
                increasing = not increasing
                parts.append((per, i - 1))
                per = i - 1
            else:
                i += 1
    if len(parts) == 0 or parts[-1][1] != n-1:
        parts.append((per, n-1))
    # print(parts)
    new_parts = []
    arr_maxi = [0] * (maxi + 1)
    arr_rem = [0] * (maxi + 1)
    for part in parts:
        temp_maxi = -1
        for j in range(part[0], part[1]+1):
            temp_maxi = max(temp_maxi, arr[j])
        new_parts.append((temp_maxi, arr[part[0]], arr[part[1]]))
        arr_maxi[temp_maxi] += 1
    
    for i in range(len(new_parts) - 1):
        arr_rem[new_parts[i][2]] += 1
    
    # print(new_parts)
    # print(arr_maxi)
    # print(arr_rem)
    
    for i in range(1, maxi+1):
        arr_maxi[i] += arr_maxi[i-1]
        arr_rem[i] += arr_rem[i-1]

    # print(arr_maxi)
    # print(arr_rem)
    ans_arr = []
    for k in range(1, maxi+1):
        ans = 0
        for j in range(k, maxi+1, k):
            ans = ans + (arr_maxi[j] - arr_maxi[j-k]) * (j // k)
            ans = ans - (arr_rem[j] - arr_rem[j-k]) * (j // k)
        if maxi % k != 0:
            temp = maxi // k * k
            # print(k, temp, maxi // k + 1)
            ans = ans + (arr_maxi[maxi] - arr_maxi[temp]) * (maxi // k + 1)
            ans = ans - (arr_rem[maxi] - arr_rem[temp]) * (maxi // k + 1)
        ans_arr.append(ans)
    print(*ans_arr)
    return ans_arr

n = int(input())
arr = list(map(int, input().split()))
solve(n, arr)


def brute(n, arr):
    arr_ans = []
    required = [0] * n
    for k in range(1, max(arr) + 1):
        temp_arr = arr[:]
        ans = 0
        while temp_arr != required:

            maxi_ind = temp_arr.index(max(temp_arr))
            ans += 1
            for i in range(maxi_ind, n):
                if temp_arr[i] > 0:
                    temp_arr[i] = max(0, temp_arr[i] - k)
                else:
                    break
            for i in range(maxi_ind-1, -1, -1):
                if temp_arr[i] > 0:
                    temp_arr[i] = max(0, temp_arr[i] - k)
                else:
                    break
        arr_ans.append(ans)
    print(*arr_ans)
    return arr_ans


# n = int(input())
# arr = list(map(int, input().split()))
# brute(n, arr)

import random
def checker():
    n = 15
    for i in range(100):
        arr = [random.randint(1, 20) for i in range(n)]
        if brute(n, arr) != solve(n, arr):
            print(*arr)
            print("Found")
            print("---------brute-----------")
            brute(n, arr)
            print("---------solve-----------")
            solve(n, arr)
            break

# checker()


