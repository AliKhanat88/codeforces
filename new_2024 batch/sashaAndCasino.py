from math import ceil

for t in range(int(input())):
    k, x, a = map(int, input().split())
    sumi = 1
    temp_a = a
    j = 1
    for i in range(x):
        temp_a -= sumi
        sumi = (ceil((a - temp_a + 1) / (k-1)))
    # print(temp_a, a, k)
    if temp_a * (k) >= a+1:
        print("YES")
    else:
        print("NO")
