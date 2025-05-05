from math import ceil
def print_max(s):
    n = len(s)
    if s == n * "1":
        print(n * n)
        return
    count = 0
    maxi = 0
    for i in range(n):
        if s[i] == "1":
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    c2 = 0
    for i in range(n):
        if s[i] == "1":
            c2 += 1
        else:
            break
    maxi = max(maxi, c2 + count)
    maxi = max(count, maxi)
    if maxi % 2 == 1:
        temp = ceil(maxi / 2)
        print(temp*temp)
        return
    if maxi % 2 == 0:
        temp = int(maxi / 2)
        print(temp * (temp+1))
        return
    


for t in range(int(input())):
    s = input()
    print_max(s)
