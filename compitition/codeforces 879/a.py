from math import ceil
def sol():
    # print("test case")
    n = int(input())
    arr = input().split()
    count_1 = 0
    count1 = 0
    for num in arr:
        if num == "-1":
            count_1 += 1
        else:
            count1 += 1
    # print(count_1, count1)
    if count1 < count_1:
        temp = ceil((count_1 - count1) / 2)
        count_1 = count_1 - temp
    else:
        temp = 0
    if count_1 % 2 == 1:
        print(temp+1)
    else:
        print(temp)
for t in range(int(input())):
    sol()
