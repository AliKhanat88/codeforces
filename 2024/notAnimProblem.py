import sys
input = sys.stdin.readline

N = 10000001
grr = [0] * N
grr[1] = 1
per = 2
for i in range(3, N, 2):
    if grr[i] == 0:
        grr[i] = per
        per += 1
    for j in range(i + 2* i, N, 2 * i):
        if grr[j] == 0:
            grr[j] = grr[i]

# print(grr[9])

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans ^= (grr[arr[i]])
    if ans == 0:
        print("Bob")
    else:
        print("Alice")
for t in range(int(input())):
    solve()