from blackCells import solve
from random import randint


def temp(n, k, l, r):
    # n,k=map(int,input().split())
    # l=list(map(int,input().split()))
    # r=list(map(int,input().split()))
    cnt=0
    one=0
    ans=pow(2,61)-1
    for i in range(n):
        cnt+=r[i]-l[i]+1
        if r[i]==l[i]:
            one+=1
        if cnt>=k:
            ans=min(ans,r[i]-(cnt-k)+(i+1)*2-min(one,(cnt-k)))
    if cnt<k:
        print(-1)
        return -1
    else:
        print(ans)
        return ans



def valid():
    n = 20
    k = 20
    per = 1
    for i in range(100000000):
        arr = []
        brr = []
        per = 1
        for j in range(n):
            arr.append(randint(per, per + 3))
            per = arr[-1]
            brr.append(randint(per, per + 3))
            per = brr[-1] + 1
        if solve(n, k, arr, brr) != temp(n, k, arr, brr):
            print(arr ,brr)
            print(solve(n, k, arr, brr), temp(n, k, arr, brr))
            return

valid()