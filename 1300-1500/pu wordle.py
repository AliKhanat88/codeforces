from collections import Counter

def check(dict1, dict2):
    for key, val in dict1.items():
        if dict1[key] > dict2[key]:
            return False
    return True

def solve():
    a = input()
    b = input()
    c1 = Counter(list(b))
    c2 = Counter()
    i = 0
    j = 0
    mini = 99999999999999999
    mini_str = ""
    while i < len(a):
        c2[a[i]] += 1
        if check(c1, c2):
            while j <= i:
                c2[a[j]] -= 1
                if check(c1, c2):
                    j += 1
                else:
                    c2[a[j]] += 1
                    break
            if i - j + 1 <= mini:
                mini = i - j + 1
                mini_str = a[j:i+1]
        # print(i)
        # print(c1)
        # print(c2)
        # print("mini", mini)
        # print("mini_str", mini_str)
        i += 1
    print(mini_str)




for t in range(int(input())):
    solve()