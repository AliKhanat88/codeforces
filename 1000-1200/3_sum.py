from collections import defaultdict

def is_poss(n, arr):
    if n == 3:
        temp = sum(arr)
        if temp == arr[0] or temp == arr[1] or temp == arr[2]:
            print("YES")
        else:
            print("NO")
    elif n == 4:
            if arr[0] + arr[1] + arr[2] in arr:
                if arr[0] + arr[1] + arr[3] in arr:
                    if arr[1] + arr[2] + arr[3] in arr:
                        if arr[0] + arr[2] + arr[3] in arr:
                            print("YES")
                            return
            print("NO")
    else:
        dict = defaultdict(lambda:0)
        for i in range(n):
            dict[arr[i]] += 1
            if len(dict) > 3:
                print("NO")
                return
        keys = list(dict.keys())
        if len(dict) == 1 and keys[0] == 0:
            print("YES")
            return
        if len(dict) == 2:
            if keys[0] == 0:
                if dict[keys[1]] == 1:
                    print("YES")
                    return
            elif keys[1] == 0:
                if dict[keys[0]] == 1:
                    print("YES")
                    return
        if len(dict) == 3:
            if keys[0] == 0 or keys[1] == 0 or keys[2] == 0:
                keys.remove(0)
                if keys[0] == -keys[1] and dict[keys[0]] == 1 and dict[keys[1]] == 1:
                    print("YES")
                    return
        print("NO")

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    is_poss(n, arr)