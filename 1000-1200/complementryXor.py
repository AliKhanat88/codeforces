def solve():
    n = int(input())
    a = input()
    b = input()
    if n == 1:
        if b == "1":
            print("NO")
            return
        elif a == "1":
            print("YES")
            print(1)
            print(1, 1)
            return
        else:
            print("YES")
            print(0)
            return
    ones = 0
    zeros = 0
    set_1 = set()
    set_0 = set()
    output_1 = []
    output_0 = []
    for i, char in enumerate(a):
        if char == "1":
            output_1.append(i+1)
            ones += 1
            set_1.add(b[i])
        else:
            output_0.append(i+1)
            zeros += 1
            set_0.add(b[i])
    set_0 = list(set_0)
    set_1 = list(set_1)
    if len(set_1) > 1 or len(set_0) > 1 or(len(set_0) != 0 and len(set_1) != 0 and set_0[0] == set_1[0]):
        print("NO")
        return
    print("YES")
    if (ones % 2 == 1 and set_1[0] == "0") or (ones % 2 == 0 and len(set_1) != 0 and set_1[0] == "1"):
        print(ones)
        for num in output_1:
            print(f"{num} {num}")
    elif (zeros % 2 == 1 and set_0[0] == "0") or (zeros % 2 == 0 and len(set_0) != 0 and set_0[0] == "1"):
        print(zeros + 1)
        for num in output_0:
            print(f"{num} {num}")
        print(1, n)
    elif ones == 0 and set_0[0] == "0":
        print(0)
    elif zeros == 0 and set_1[0] == "0":
        print(1)
        print(1, n)
    else:
        print(zeros+2)
        for num in output_0:
            print(f"{num} {num}")
        print(1, 1)
        print(2, n)




for t in range(int(input())):
    solve()