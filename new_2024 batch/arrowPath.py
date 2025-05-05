def solve():
    # print("TEST")
    n = int(input())

    arr = [0] * 2
    arr[0] = list(input())
    arr[1] = list(input())
    isTrueFirst = False
    isTrueSecond = False
    i = 0
    j = 1 
    # print(arr)
    while j < n:
        # print(i,j,arr[i][j])
        if isTrueFirst == True and isTrueSecond == True:
            print("NO")
        if arr[i][j] == "<" and i == 0 and isTrueFirst == True:
            print("NO")
            return
        if arr[i][j] == "<" and i == 1 and isTrueSecond == True:
            print("NO")
            return
        if arr[i][j] == "<":
            # print(i, j , arr[i][j])
            i = (i + 1) % 2
            j = j - 1
            if i == 0:
                isTrueFirst = True
            else:
                isTrueSecond = True
        elif arr[i][j] == ">":
            j += 2
            isTrueFirst = False
            isTrueSecond = False
    print("YES")
for t in range(int(input())):
    solve()

