from collections import defaultdict, Counter

price = defaultdict(lambda:4)

for i in range(1, 11):
        price[(i, i)] = 0

dict = {
    1: "QQQ",
    2: "WWW",
    3: "EEE",
    4: "QQW",
    5: "QQE",
    6: "QWW",
    7: "WWE",
    8: "QEE",
    9: "WEE",
    10: "QWE"
}

for i in range(1, 11):
    for j in range(1, 11):
        if i != j:
            if dict[i][1] + dict[i][2] == dict[j][0] + dict[j][1]:
                price[(i, j)] = 2
            elif dict[i][2] == dict[j][0]:
                price[(i, j)] = 3

print(price)

def solve():
    c = int(input())
    per = [[60, 0]]
    for i in range(c):
        n = int(input())
        arr = list(map(int, input().split()))
        new_per = []
        counti = Counter(arr)
        for key, val in counti.items():
            mini = float("inf")
            for peri in per:
                mini = min(mini, price[(peri[0], key)] + val + peri[1])
            remain = list(counti.keys())
            remain.remove(key)
            for last in remain:
                ans = mini
                temp_remain = remain[:]
                temp_remain.remove(last)
                last_open = key
                while len(temp_remain) != 0:
                    mini2 = float("inf")
                    mini2_ind = None
                    for j in range(len(temp_remain)):
                        if price[(last_open, temp_remain[j])] < mini2:
                            mini2 = price[(last_open, temp_remain[j])]
                            mini2_ind = j
                    ans += price[(last_open, temp_remain[mini2_ind])] + counti[temp_remain[mini2_ind]]
                    last_open = temp_remain.pop(mini2_ind)
                ans += price[(last_open, last)] + counti[last]
                done = False
                for j, num in enumerate(new_per):
                    if num[0] == last:
                        new_per[j][1] = min(new_per[j][1], ans)
                        done = True
                if done == False:
                    new_per.append([last, ans])
        print(new_per, i)
        per = new_per
    print(new_per)



    



solve()