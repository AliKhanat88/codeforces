def solve():
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    for i in range(1, n+1):
        ans = []
        length = n // i
        if n % i == 0 and length >= 3:
            for j in range(i):
                done = True
                diff = arr[j+i] - arr[j]
                temp = [arr[j], arr[j+i]]
                for k in range(j+i+i, n, i):
                    if arr[k] - arr[k-i] != diff:
                        done = False
                        break
                    temp.append(arr[k])
                if done == True:
                    ans.append((temp, "AP"))
                else:
                    done = True
                    diff = arr[j+i] / arr[j]
                    temp = [arr[j], arr[j+i]]
                    for k in range(j+i+i, n, i):
                        if arr[k] / arr[k-i] != diff:
                            done = False
                            break
                        temp.append(arr[k])
                    if done == True:
                        ans.append((temp, "GP"))
            if len(ans) == i:
                break
    # print(ans)
    print(f"Count={len(ans)}")
    for ans1 in ans:
        print(ans1[1], end= " ")
        print(*ans1[0])
for t in range(int(input())):
    solve()