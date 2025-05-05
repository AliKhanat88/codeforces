def find_range(arr, l, r):
    maxi = 0
    sumi = 0
    for i in range(l, r+1):
        sumi += arr[i]
        sumi = max(sumi , 0)
        maxi = max(maxi, sumi)
    
    mini = 0
    sumi = 0
    for i in range(l, r+1):
        sumi += arr[i]
        sumi = min(sumi, 0)
        mini = min(mini, sumi)
    
    return mini, maxi


def solve(n, arr):
    
    other = None
    if max(arr) not in (-1, 1):
        other = max(arr)
    if min(arr) not in (-1, 1):
        other = min(arr)
    
    if other == None:
        mini, maxi = find_range(arr, 0, n-1)
        print(maxi - mini + 1)
        print(*[i for i in range(mini, maxi+1)])
        return
    
    seti = set()
    index = arr.index(other)
    l1, r1 = find_range(arr, 0, index-1)
    l2, r2 = find_range(arr, index+1, n-1)
    # print(index+1, n-1)
    # print(l1, r1)
    # print(l2, r2)
    for i in range(l1, r1+1):
        seti.add(i)
    for i in range(l2, r2+1):
        seti.add(i)
    maxi1 = 0
    mini1 = 0
    sumi = 0
    for i in range(index-1, -1, -1):
        sumi += arr[i]
        maxi1 = max(maxi1, sumi)
        mini1 = min(mini1, sumi)
    
    maxi2 = 0
    mini2 = 0
    sumi = 0
    for i in range(index+1, n):
        sumi += arr[i]
        maxi2 = max(maxi2, sumi)
        mini2 = min(mini2, sumi)
    # print(mini1, mini2, maxi1, maxi2, "here")
    for i in range(mini1 + mini2, maxi1 + maxi2 + 1):
        seti.add(i + other)

    print(len(seti))
    print(*sorted(list(seti)))
    return sorted(list(seti))

def brute(n, arr):
    seti = set()
    seti.add(0)
    for i in range(n):
        for j in range(i, n):
            seti.add(sum(arr[i:j+1]))
    print(len(seti))
    print(*sorted(list(seti)))
    return sorted(list(seti))



import random
def check():
    for i in range(100):
        n = 5
        arr = []
        can = True
        for i in range(n):
            if can:
                temp = random.choice([-1, 1, random.randint(-50, 50)])
            else:
                temp = random.choice([-1, 1])
            if temp not in (-1, 1):
                can = False
            arr.append(temp)
        if brute(n, arr) != solve(n, arr):
            print("FOund")
            print(n)
            print("solve")
            # print(arr)
            print(solve(n, arr))
            print("brute")
            # print(arr)
            print(brute(n, arr))
            break
# check()
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n ,arr)
