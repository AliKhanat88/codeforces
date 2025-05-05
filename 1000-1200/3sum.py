from collections import defaultdict
def print_poss(n, arr):
    dict = defaultdict(lambda:0)
    num_arr = []
    for i in range(n):
        if dict[arr[i]] < 3:
            num_arr.append(arr[i])
            dict[arr[i]] += 1

    n = len(num_arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if str(num_arr[i] + num_arr[j] + num_arr[k])[-1] == "3":
                    print("YES")
                    return
    print("NO") 

for t in range(int(input())):
    n = int(input())
    arr = [int(num[-1]) for num in input().split()]
    print_poss(n, arr)