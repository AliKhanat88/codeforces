from collections import Counter

def solve():
    i =Counter()
    r =Counter()
    n = int(input())
    s = input()
    dict =Counter(s)
    # print("TEST")
    # print(dict)
    done = False
    if dict["E"] >= 2:
        i["E"] += 1
        r["E"] += 1
        dict["E"] -= 2
        done = True
    elif dict["W"] >= 2:
        i["W"] += 1
        r["W"] += 1
        dict["W"] -= 2
        done = True
    elif dict["N"] >= 2:
        i["N"] += 1
        r["N"] += 1
        dict["N"] -= 2
        done = True
    elif dict["S"] >= 2:
        i["S"] += 1
        r["S"] += 1
        dict["S"] -= 2
        done = True
    if done == True:
        donei = True
        doner = True
    else:
        donei = False
        doner = False

    if dict["E"] >= 1 and dict["W"] >= 1 and donei == False:
        i["E"] += 1
        i["W"] += 1
        dict["E"] -= 1
        dict["W"] -= 1
        donei = True
    if dict["N"] >= 1 and dict["S"] >= 1 and donei == False:
        i["N"] += 1
        i["S"] += 1
        dict["N"] -= 1
        dict["S"] -= 1
        donei = True
    if dict["N"] >= 1 and dict["S"] >= 1 and doner == False:
        r["N"] += 1
        r["S"] += 1
        dict["N"] -= 1
        dict["S"] -= 1
        doner = True
    if dict["E"] >= 1 and dict["W"] >= 1 and doner == False:
        r["E"] += 1
        r["W"] += 1
        dict["E"] -= 1
        dict["W"] -= 1
        doner = True
    if donei == False or doner == False:
        print("NO")
        return
    if dict["E"] >= dict["W"]:
        dict["E"] -= dict["W"]
        i["W"] += dict["W"]
        i["E"] += dict["W"]
        dict["W"] = 0
        if dict["E"] % 2 != 0:
            print("NO")
            return
        else:
            i["E"] += (dict["E"] // 2)
            r["E"] += (dict["E"] // 2)
    elif dict["E"] < dict["W"]:
        dict["W"] -= dict["E"]
        i["W"] += dict["E"]
        i["E"] += dict["E"]
        dict["E"] = 0
        if dict["W"] % 2 != 0:
            print("NO")
            return
        else:
            i["W"] += (dict["W"] // 2)
            r["W"] += (dict["W"] // 2)

    if dict["N"] >= dict["S"]:
        dict["N"] -= dict["S"]
        i["S"] += dict["S"]
        i["N"] += dict["S"]
        dict["S"] = 0
        if dict["N"] % 2 != 0:
            print("NO")
            return
        else:
            i["N"] += dict["N"] // 2
            r["N"] += dict["N"] // 2
    elif dict["N"] < dict["S"]:
        dict["S"] -= dict["N"]
        i["S"] += dict["N"]
        i["N"] += dict["N"]
        dict["N"] = 0
        if dict["S"] % 2 != 0:
            print("NO")
            return
        else:
            i["S"] += dict["S"] // 2
            r["S"] += dict["S"] // 2
    # print(s)
    # print(i)
    # print(r)
    for j in range(n):
        if i[s[j]] > 0:
            print("H", end="")
            i[s[j]] -= 1
        else:
            print("R", end="")
            r[s[j]] -= 1
    print()
        
    

for t in range(int(input())):
    solve()

