from robinHoodArchery import solve
from random import randint
import sys
input = sys.stdin.readline
import heapq

def process_queries(n, a, queries):
def check(i):
    if i < 0 or i >= n-1:return 0
    sc = 0
    while B[erarliest[i][0]] != i:
        heapq.heappop(erarliest[i])
    while B[erarliest[i+1][0]] != i+1:
        heapq.heappop(erarliest[i+1])
    if erarliest[i][0] > erarliest[i+1][0]:
        sc += 1
    return sc

for _ in range(int(input())):
    n,m,q = map(int,input().split())
    T = [0] * n
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(n):
        T[A[i]-1] = i
    B = [T[i-1] for i in B] + list(range(n))
    erarliest = [[] for _ in range(n)]
    for i, j in enumerate(B):
        heapq.heappush(erarliest[j], i)
    ok = 0
    for i in range(n-1):
        if erarliest[i][0] > erarliest[i+1][0]:
            ok += 1
    for x in range(q+1):
        if ok == 0:
            print("YA")
        else:
            print("TIDAK")
        if x==q:break
        a,b = map(int,input().split())
        b-=1
        b = T[b]
        a-= 1
        old = B[a]
        z = {old,old-1,b,b-1}
        for i in z:
            ok -= check(i)
        B[a] = b
        heapq.heappush(erarliest[b],a)
        for i in z:
            ok += check(i)



def main():
    n = 100
    for i in range(100000):

        arr = [randint(1, 20) for i in range(n)]
        queries1 = []
        queries2 = []
        for j in range(5):
            temp = randint(1, n)
            temp2 = randint(temp, n)
            queries1.append((temp - 1, temp2 - 1, j))
            queries2.append((temp, temp2))
        if solve(n, len(queries1), arr, queries1) != process_queries(n, arr, queries2):
            print(arr)
            print(queries2)
            print(queries1)
            print(solve(n, len(queries1), arr, queries1), process_queries(n, arr, queries2))
            break
main()
