def solve():
    a = list(input())
    b = list(input())
    is_a_g = False
    # print("TEST")
    index = 0
    for i in range(len(a)):
        # print(a[i], b[i])
        if int(a[i]) > int(b[i]):
            is_a_g = True
            index = i
            break
        elif int(a[i]) < int(b[i]):
            is_a_g = False
            index = i
            break
    # print(is_a_g)
    for i in range(index + 1, len(a)):
        if is_a_g:
            if int(a[i]) > int(b[i]):
                a[i], b[i] = b[i], a[i]
        else:
            if int(a[i]) < int(b[i]):
                a[i], b[i] = b[i], a[i]

    print("".join(a))
    print("".join(b))
for i in range(int(input())):
    solve()