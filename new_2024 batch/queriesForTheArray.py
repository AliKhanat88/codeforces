def solve():
    stri = input()
    # print("TEST")
    # print(stri)
    s = []
    for char in stri:
        if len(s) <= 1 and char == "0":
            print("NO")
            return
        if char == "0":
            if len(s) != 0 and s[-1] == 1:
                print("NO")
                return
            s[-1] = 0
        elif char == "1":
            j = len(s) - 1
            # s[-1] == 1
            while j > -1:
                if s[j] == -1:
                    s[j] = 1
                elif s[j] == 0:
                    print("NO")
                    return
                else:
                    break
                j -= 1 

        elif char == "+":
            s.append(-1)
        elif char == "-":
            s.pop()
        # print(f"stack: {s}")
        # print(f"cur count: {cur_count}")
    print("YES")


for t in range(int(input())):
    solve()