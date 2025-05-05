num = 100001
lowest_Mult = [0] * (num)

for i in range(2, num):
    for j in range(i, num, i):
        lowest_Mult[j] = lowest_Mult[j] + 1
sumi = 0
for i in range(num):
    sumi = sumi + lowest_Mult[i] * lowest_Mult[i]
print(sumi)