from collections import defaultdict

def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda:0)
    for num in arr:
        dict[num] += 1
    per = dict[0]
    for i in range(1, 101):
        if dict[i] > per:
            print("NO")
            return
        per = dict[i]
    print("YES")

for t in range(int(input())):
    sol()