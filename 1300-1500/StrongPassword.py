
def solve():
    s = input()
    n = int(input())
    l = list(map(int, list(input())))
    r = list(map(int, list(input())))
    k = 0
    i = 0
    while i < n:
        arr = [j for j in range(l[i], r[i] +1)]
        # print(arr)
        while k < len(s):
            if int(s[k]) in arr:
                arr.remove(int(s[k]))
                # print(k)
                if len(arr) == 0:
                    k += 1
                    break
            k += 1
        if k >= len(s):
            break
        i += 1
    if i < n -1 or len(arr) != 0:
        print("YES")
    else:
        print("NO")
        
            


for t in range(int(input())):
    solve()