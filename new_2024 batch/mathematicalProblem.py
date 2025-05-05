def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n == 3:
        print(169)
        print(196)
        print(961)
    else:
        ans1 = ["1", "3"] + list("0" * ((n - 3) // 2))
        # print(ans1)
        print(int("".join(ans1)) ** 2)
        for i in range(2, len(ans1)):
            ans1[i], ans1[i-1] = ans1[i-1], ans1[i]
            print(int("".join(ans1)) ** 2)
        print("196" + "0" * (n-3))
        ans1 = ["3", "1"] + list("0" * ((n - 3) // 2))
        print(int("".join(ans1)) ** 2)
        for i in range(2, len(ans1)):
            ans1[i], ans1[i-1] = ans1[i-1], ans1[i]
            print(int("".join(ans1)) ** 2)



for t in range(int(input())):
    solve()