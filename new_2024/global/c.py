import sys
input = sys.stdin.readline

def compare(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return True
        elif b[i] < a[i]:
            return False
    if len(a) >= len(b):
        return True
    else:
        return False

def solve():
    arr = list(map(int, list(input().strip())))
    length = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            length = n - i - 1
        else:
            break
    # print(length)
    if length == 0:
        print(1, n, 1, 1)
        return
    cur = []
    cur_val = -1
    for i in range(n):
        if i + length - 1 < n and arr[i] == 1:
            new_arr = []
            ind = n - length
            for j in range(i , i + length):
                if arr[j] != arr[ind]:
                    new_arr.append(ind)
                ind += 1
            # print(new_arr)
            # print(i)
            if compare(new_arr, cur):
                cur = new_arr
                cur_val = i
    print(1, n, cur_val + 1, cur_val + length)


for t in range(int(input())):
    solve()