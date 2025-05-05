
import heapq


def main(n,m,q,A, B,queries):
# def main():
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
    # print(f.read())
    import sys
    f = open("input1.txt", "r")
    input = f.readline
    # for _ in range(int(input())):
    # n,m,q = map(int,input().split())
    T = [0] * n
    # A = list(map(int,input().split()))
    # B = list(map(int,input().split()))
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
    ans = []
    for x in range(q+1):
        if ok == 0:
            # print("YA")
            ans.append("YA")
        else:
            # print("TIDAK")
            ans.append("TIDAK")
        if x==q:break
        a,b = queries[x]
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
    return ans
if __name__ == "__main__":
    main()



