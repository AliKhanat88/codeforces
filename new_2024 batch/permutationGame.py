def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    i = 1
    j = n
    a = 0
    b = 0
    c = 0
    for num in arr:
        if num != i and num == j:
            a += 1
        elif num != j and num == i:
            b += 1
        elif num != i and num != j:
            c += 1
        i += 1
        j -= 1
    # print(a, b, c)

    if a <= b:
        if a + c <= b:
            print("First")
        else:
            print("Tie")
    else:
        if b + c < a:
            print("Second")
        else:
            print("Tie")

for t in range(int(input())):
    solve()