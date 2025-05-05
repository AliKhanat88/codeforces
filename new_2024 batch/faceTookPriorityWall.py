from collections import defaultdict

name = input()
n = int(input())
dict = defaultdict(lambda:0)
for i in range(n):
    temp = input().split()
    if temp[1] == "posted":
        if temp[0] == name or temp[3][:-2] == name:
            dict[temp[0]] += 15
            dict[temp[3][:-2]] += 15
        else:
            dict[temp[0]] += 0
            dict[temp[3][:-2]] += 0
    if temp[1] == "commented":
        if temp[0] == name or temp[3][:-2] == name:
            dict[temp[0]] += 10
            dict[temp[3][:-2]] += 10
        else:
            dict[temp[0]] += 0
            dict[temp[3][:-2]] += 0
    if temp[1] == "likes":
        if temp[0] == name or temp[2][:-2] == name:
            dict[temp[0]] += 5
            dict[temp[2][:-2]] += 5
        else:
            dict[temp[0]] += 0
            dict[temp[2][:-2]] += 0

a = sorted(dict.items(), key=lambda x:(-x[1], x[0]))

for key, val in a:
    if key != name:
        print(key)

