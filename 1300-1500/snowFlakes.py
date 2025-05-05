arr = [0] * 1000000
for i in range(2, 1000):
    sumi = i ** 2 + i + 1
    j = 3
    while sumi <= 1000000:
        arr[sumi-1] = 1
        sumi = sumi + i ** j
        j += 1

for t in range(int(input())):
    n = int(input())
    if arr[n-1] == 1:
        print("YES")
    else:
        print("NO")