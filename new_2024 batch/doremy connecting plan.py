def solve():
    n, c = map(int, input().split())

    arr = input().split()

    arr_temp = [(int(arr[i]), i+1) for i in range(n)]
    sumi = arr_temp[0][0]
    arr_temp.pop(0)
    arr_temp.sort(key=lambda x: x[0]/(c*x[1]), reverse=True)
    # print("TEST")
    # print(arr_temp)
    mini = 1
    for i in range(n-1):
        if (mini * arr_temp[i][1] * c) > sumi + arr_temp[i][0]:
            print("NO")
            return
        mini = min(mini, arr_temp[i][1])
        sumi = sumi + arr_temp[i][0]
    print("YES")

    


for t in range(int(input())):
    solve()

