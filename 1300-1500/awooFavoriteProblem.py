def solve():
    n = int(input())
    dict = {
        "a": "b",
        "b": "c",
        "c": None
    }
    # index_a = [0] * n
    # index_b = [0] * n
    # for 
    s = list(input())
    r = list(input())
    done = True
    per = None
    times = 0
    for i in range(n):
        # print(per, done, times)
        if done == False:
            if s[i] == per[1]:
                s[i] = per[0]
                times -= 1
                if times == 0:
                    done = True
            elif s[i] != per[0]:
                print("NO")
                return

            
        if s[i] != r[i]:
            if dict[s[i]] == r[i]:
                new_per = (s[i], r[i])
                s[i] = r[i]
            else:
                print("NO")
                return
            if done == False:
                if new_per != per:
                    print("NO")
                    return
                else:
                    times += 1
            else:
                times = 1
            per = new_per
            done = False

        # print(s, r)
    if done == True:
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    solve()