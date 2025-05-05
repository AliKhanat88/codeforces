def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    per = False
    cost = 0
    sumi = 0
    for i in range(n):
        if arr[i] < 0:
            if per == False:
                cost += 1
                per = True
        elif arr[i] > 0:
            per = False
        sumi += abs(arr[i])
    print(sumi, cost)

for t in range(int(input())):
    sol()
    
