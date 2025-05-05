from collections import defaultdict

def print_min(s, n):
    dict = defaultdict(lambda: -1)
    back_arr = [0] * n
    for j in range(n-1, -1, -1):
        back_arr[j] = dict[s[j]]
        dict[s[j]] = j
    # print(back_arr)
    count = 0
    per = None
    for i in range(n):
        if per == None:
            if back_arr[i] == -1:
                count += 1
            else:
                per = back_arr[i]
        else:
            if s[per] == s[i]:
                per = None
            elif back_arr[i] < per and back_arr[i] != -1:
                per = back_arr[i]
                count += 1
            else:
                count += 1
    print(count)       

for t in range(int(input())):
    s = input()
    print_min(s, len(s))