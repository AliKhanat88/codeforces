from copy import deepcopy

def recur(n, arr, corners,index=0):
    
    if index > 3:
        for i in range(4):
            if corners[i] + corners[(i+1)%4] > arr[i]:
                return False
        return True
    else:
        # print(n, arr[index], corners) 
        if arr[index] == n:
            temp_cor = deepcopy(corners)
            temp_cor[index] = 1
            temp_cor[(index+1)%4] = 1
            return recur(n, arr, temp_cor,index+1)
        elif arr[index] == n-1:
            temp_cor = deepcopy(corners)
            temp_cor[index] = 1
            ans1 = recur(n, arr, temp_cor,index+1)
            temp_cor = deepcopy(corners)
            temp_cor[(index+1)%4] = 1
            ans2 = recur(n, arr, temp_cor,index+1)
            if ans1 == True or ans2 == True:
                return True
            else:
                return False
        else:
            return recur(n, arr, deepcopy(corners),index+1)
def solve():
    n, u, r, d, l = map(int, input().split())
    arr = [u,r,d,l]
    corners = [0, 0, 0, 0]
    if recur(n, arr, corners):
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    solve()