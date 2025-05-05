def solve():
    n = int(input())
    arr = list(map(int, list(input())))
    sumi = 0
    for i in range(n):
        j = i
        c1 = 0
        count = [0]*10
        while i-j <= 100 and j>=0:
            if count[arr[j]] == 0:
                c1 += 1
            count[arr[j]] += 1
            if c1 >= max(count):
                sumi += 1
            j -= 1
    print(sumi)
for t in range(int(input())):
    solve()