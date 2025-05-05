from math import lcm, ceil

def solve():
    n = int(input())
    s = input()
    dict = {'+':0, "-":0}
    for i in range(n):
        dict[s[i]] += 1
    maxi = max(dict["+"], dict["-"])
    mini = min(dict["+"], dict["-"])
    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        # print(a, b)
        # if dict["+"] == dict["-"]:
        #     print("YES")
        #     continue
        temp_1 = lcm(a, b) // max(a,b)
        temp_2 = lcm(a, b) // min(a,b)
        # print(temp_1, dict["+"])
        # print(temp_2, dict["-"])
        # print((maxi - mini) / temp_1)
        diff = maxi - mini
        # print(diff)
        # print(temp_2 - temp_1)
        if temp_2 - temp_1 == 0:
            if diff == 0:
                print("YES")
            else:
                print("NO")
        elif diff % (temp_2 - temp_1) == 0 and abs(diff // (temp_2 - temp_1)) * temp_1 <= mini and abs(diff // (temp_2 - temp_1)) * temp_2 <= maxi:
            print("YES")
        else:
            print("NO")


solve()