other1 = {1, 2, 4, 8, 16, 13, 17, 19}
other2 = {3, 6, 12, 14, 18, 7, 9, 11}

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    other1_ch = False
    other2_ch = False
    zero = False
    for i in range(n):
        if arr[i] % 10 == 5:
            arr[i] = arr[i] + 5
            zero = True
        elif arr[i] % 10 == 0:
            zero = True
        elif arr[i] % 20 in other1:
            other1_ch = True
        elif arr[i] % 20 in other2:
            other2_ch = True

    if len(set(arr)) == 1:
        print("YES")
    else:
        if zero == False:
            if other1_ch == True and other2_ch == True:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
    # print(arr)
             
        
        


for t in range(int(input())):
    solve()