import sys 
sys.setrecursionlimit(1000)

def recur(count, sumi, arr, sol):
    if count == 0:
        if sumi == 0:
            return True
        else:
            return False
    temp1 = 0
    temp2 = 0
    for i in range(count):
        temp1 += arr[i]
        temp2 += arr[len(arr) - i - 1]
    # print(f"Count: {count}, Sumi: {sumi},{arr},{sol}, temp1: {temp1}, {temp2}")
    if sumi > temp1 or sumi < temp2:
        return False
    else:
        while len(arr) >= count:
            temp = arr.pop()
            sol.append(temp)
            if recur(count-1, sumi - temp, arr, sol):
                return True
            else:
                sol.pop()

def solve():
    n, l ,r, sumi = map(int, input().split())
    sol = []
    arr = [n-i for i in range(n)]
    # print("TEST")
    # print(n,l,r,sumi)
    # print(arr)
    if recur(r-l+1, sumi, arr, sol) == False:
        print(-1)
        return
    # print(sol)
    ans = set(sol)
    j = 1
    for i in range(l-1):
        while j in ans:
            j += 1
        print(j, end=" ")
        j += 1
    print(*sol, end=" ")
    for i in range(r+1, n+1):
        while j in ans:
            j += 1
        print(j, end=" ")
        j += 1
    print()
    
    


for i in range(int(input())):
    solve()