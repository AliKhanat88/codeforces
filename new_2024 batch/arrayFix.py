def solve():
    n = int(input())
    arr = input().split()

    per = int(arr[-1])
    for i in range(n-2, -1, -1):
        # print(arr[i])
        if int(arr[i]) > per:
            for j in range(len(arr[i])-1, -1, -1):
                if int(arr[i][j]) > per:
                    print("NO")
                    return
                per = int(arr[i][j])
        else:
            per = int(arr[i])
    print("YES")

for t in range(int(input())):
    solve()

