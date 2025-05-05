import sys
input= sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    data = [[] for i in range(k)]
    for i in range(k):
        data[i] = list(map(int, input().split()))
    # print("TEST")
    if n <= 2 or k == 1:
        print("YES")
        return
    if k >= 1:
        arr1 = data[0][:]
    if k >= 2:
        arr2 = data[1][:]
        if arr1[1] == arr2[0]:
            right = arr1[2]
            left = -1
        elif arr1[-1] == arr2[0]:
            left = arr1[-2]
            right = -1
        else:
            for i in range(2, n-1):
                if arr1[i] == arr2[0]:
                    left = arr1[i-1]
                    right = arr1[i+1]
        done = False
        if arr2[1] == right:
            arr2.insert(1, arr2[0])
            done = True
        elif arr2[-1] == left:
            arr2.insert(n, arr2[0])
            done = True
        else:
            for i in range(2, n):
                if arr2[i-1] == left and arr2[i] == right:
                    arr2.insert(i, arr2[0])
                    done = True
        if done == False and arr1.index(arr2[0]) != arr2.index(arr1[0]):
            print("NO")
            return
        
        if done == False and arr1.index(arr2[0]) == arr2.index(arr1[0]):
            arr2.insert(arr1.index(arr2[0]), arr2[0])
            temp3 = arr2.pop(0)
            # print(arr2, temp3, arr1[0])
            if k >= 3:
                arr3 = data[2]
                for i in range(2, n):
                    if arr3[i] == temp3 and arr3[i-1] == arr1[0]:
                        temp1 = arr2.index(arr1[0])
                        temp2 = arr2.index(temp3)
                        arr2[temp1], arr2[temp2] = arr2[temp2], arr2[temp1]
        if done == True:
            arr2.pop(0)
    # print(arr2, done)
    # print(arr2)
    for i in range(k):
        temp = data[i].pop(0)
        data[i].insert(arr2.index(temp), temp)
        # print(data[i])
        for j in range(n):
            if arr2[j] != data[i][j]:
                print("NO")
                return
    print("YES")



for t in range(int(input())):
    solve()