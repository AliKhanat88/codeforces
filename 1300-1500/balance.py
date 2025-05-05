from collections import defaultdict

def solve():

    q = int(input())
    dict = defaultdict(lambda:0)
    for i in range(q):
        arr = input().split()
        if arr[0] == "+":
            dict[int(arr[1])] = int(arr[1])
        else:
            arr[1] = int(arr[1])
            if dict[arr[1]] == 0:
                print(arr[1])
            else:
                temp = dict[arr[1]]
                while dict[temp] != 0:
                    temp += arr[1]
                dict[arr[1]] = temp
                print(temp)
                


solve()