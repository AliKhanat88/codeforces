def solv():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    j = 0
    while True:
        if i >= n and j >= m:
            print("Draw")
            return
        elif i >= n:
            print("Tenzing")
            return
        elif j >= m:
            print("Tsondu")
            return
        if a[i] > b[j]:
            a[i] = a[i] - b[j]
            j += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            b[j] = b[j] - a[i]
            i += 1

for t in range(int(input())):
    solv()