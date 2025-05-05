def solve():
    n = int(input())
    r1,c1,r2,c2,r3,c3 = map(int, input().split())
    x,y = map(int, input().split())
    arr = [
        [(1,1),(1,2),(2,1),1,1],
        [(n,1),(n-1,1),(n,2),n,1],
        [(1,n),(1,n-1),(2,n),1,n],
        [(n,n),(n,n-1),(n-1,n),n,n]
    ]
    for i in range(4):
        if (r1,c1) in arr[i] and (r2,c2) in arr[i] and (r3,c3) in arr[i]:
            if x == arr[i][3] or y == arr[i][4]:
                print("YES")
                return
            print("NO")
            return
    
    if r1 == r2 or r1 == r3:
        if r1 % 2 == 0:
            even_row = True
        else:
            even_row = False
    else:
        if r2 % 2 == 0:
            even_row = True
        else:
            even_row = False

    if c1 == c2 or c1 == c3:
        if c1 % 2 == 0:
            even_col = True
        else:
            even_col = False
    else:
        if c2 % 2 == 0:
            even_col = True
        else:
            even_col = False
        
    if (r1 == c2 and c1 == r2) or (r1 == c3 and c1 == r3):
        # print("in r1")
        if abs(r1 - c1) % 2 == 0:
            white = True
        else:
            white = False
    else:
        if abs(r2 - c2) % 2 == 0:
            white = True
        else:
            white = False
    if abs(x - y) % 2 == 0:
        is_white = True
    else:
        is_white = False

    if x % 2 == 0:
        is_even_row = True
    else:
        is_even_row = False
    
    if y % 2 == 0:
        is_even_col = True
    else:
        is_even_col = False
    # print(is_even_col, even_col, is_even_row, even_row, is_white, white)
    if is_even_col == even_col:
        print("YES")
    elif is_even_row == even_row:
        print("YES")
    elif is_white == white:
        print("YES")
    else:
        print("NO")


for t in range(int(input())):
    solve()