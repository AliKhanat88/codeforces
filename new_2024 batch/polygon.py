def solve():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = input()
    # print("HELl0")
    for i in range(n):
        for j in range(n):
            if i != n-1 and j != n-1:
                if data[i][j] == "1" and data[i][j+1] != "1" and data[i+1][j] != "1":
                    print("NO")
                    return
    print("YES")


for t in range(int(input())):
    solve()