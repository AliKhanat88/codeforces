def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # print("TEST")
    # print(arr)
    pair_arr = [[arr[i], i] for i in range(n)]

    pair_arr.append([-1, -1])
    pair_arr.sort(key=lambda x: x[0], reverse=True)
    lowest = n
    # print(pair_arr)
    ans = [0] * n
    val = n
    i = 0
    while i < n:
        if pair_arr[i][0] >= (i+1):
            # print(pair_arr[pair_arr[i][0] - 1][0])
            if pair_arr[pair_arr[i][0]][0] >= (i+1) or pair_arr[pair_arr[i][0] - 1][0] < (i+1):
                print("NO")
                return
            else:
                j = pair_arr[i][0]
                if j < lowest:
                    ans[pair_arr[i][1]] = val - 1
                    temp = j
                    # print(j)
                    while j < lowest:
                        ans[pair_arr[j][1]] = -val
                        j += 1
                    lowest = temp
                    # print(ans, lowest)
                    val -= 2
                else:
                    ans[pair_arr[i][1]] = val
                    val -= 1
        else:
            break
        i += 1
    for j in range(i, lowest):
        ans[pair_arr[j][1]] = -val
    print("YES")
    print(*ans)

for t in range(int(input())):
    solve()