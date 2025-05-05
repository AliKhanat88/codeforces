from pprint import pprint

def print_table(n,k,x,y):
    data = [list("." * n) for i in range(n)]
    dignols = []
    dignols.append((x-1,y-1))
    data[x-1][y-1] = "X"
    temp_x = x + 1
    temp_y = y + 1
    while temp_x <= n and temp_y <= n:
        data[temp_x-1][temp_y-1] = "X"
        dignols.append((temp_x-1,temp_y-1))
        temp_x += 1
        temp_y += 1
    temp_x = x - 1
    temp_y = y - 1
    while temp_x > 0 and temp_y > 0:
        data[temp_x-1][temp_y-1] = "X"
        dignols.append((temp_x-1,temp_y-1))
        temp_x -= 1
        temp_y -= 1
    pprint(data)
    print(dignols)

for t in range(int(input())):
    n, k, x, y = map(int, input().split())
    print_table(n,k,x,y)