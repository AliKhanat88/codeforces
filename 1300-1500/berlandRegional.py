from collections import Counter
def solve():
    n = int(input())
    unis = list(map(int, input().split()))
    skills = list(map(int, input().split()))
 
    c = Counter(unis)
    uni_skill = {}
    for key in c.keys():
        uni_skill[key] = [[0]*c[key], 0]
 
    for i in range(n):
        uni_skill[unis[i]][0][uni_skill[unis[i]][1]]= skills[i]
        uni_skill[unis[i]][1]+= 1
 
    for key in uni_skill.keys():
        uni_skill[key][0].sort(reverse=True)
        for i in range(uni_skill[key][1]-2, -1, -1):
            uni_skill[key][0][i] += uni_skill[key][0][i+1]
 
    # print(uni_skill)
    for i in range(1, n+1):
        sumi = 0
        k = 0
        keys = list(uni_skill.keys())
        while k < len(keys):
            # print(uni_skill)
            if uni_skill[keys[k]][1] % i != 0:
                sumi += uni_skill[keys[k]][0][0] - uni_skill[keys[k]][0][uni_skill[keys[k]][1] - uni_skill[keys[k]][1] % i]
            else:
                sumi += uni_skill[keys[k]][0][0]
            if i > uni_skill[keys[k]][1]:
                del(uni_skill[keys[k]])
                keys.pop(k)
            else:
                k += 1
        print(sumi, end=" ")
    print()
 
 
 
for t in range(int(input())):
    solve()