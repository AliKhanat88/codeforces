def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if len(set(arr)) == 1:
        print("NO")
        return
    print("YES")
    neg = []
    pos = []
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    neg.sort(reverse=True)
    pos.sort()
    i = 0 
    j = 0
    diff = 0
    parity = False
    while i < len(neg) or j < len(pos):
        if i >= len(neg):
            print(pos[j], end=" ")
            j += 1
            continue
        elif j >= len(pos):
            print(neg[i], end=" ")
            i += 1
            continue
        if diff >= abs(neg[i]):
            print(neg[i], end= " ")
            diff = diff + neg[i]
            i += 1
        else:
            print(pos[j], end=" ")
            diff = diff + pos[j]
            j += 1
    print()

for t in range(int(input())):
    solve()