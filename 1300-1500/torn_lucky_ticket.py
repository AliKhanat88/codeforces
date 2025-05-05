n = int(input())
arr = input().split()
count = n
one = [0] * 46
two = [0] * 46
three = [0] * 46
four = [0] * 46
five = [0] * 46
three_1 = [0] * 46
four_2 = [0] * 46
five_1 = [0] * 46
five_2 = [0] * 46

for i in range(n):
    if len(arr[i]) == 1:
        num = int(arr[i][0])
        count += 2 * (one[num]) + three_1[num] + five_2[num]
        one[num] += 1
    elif len(arr[i]) == 2:
        num = int(arr[i][0]) + int(arr[i][1])
        count +=  2 * two[num] + four_2[num]
        two[num] += 1
    elif len(arr[i]) == 3:
        num = int(arr[i][0]) + int(arr[i][1]) + int(arr[i][2])
        count +=  2 * three[num] + five_1[num]
        if num - 2 * int(arr[i][0]) > 0:
            count +=  one[num - 2 * int(arr[i][0])]
            three_1[num - 2 * int(arr[i][0])] += 1
        if num - 2 * int(arr[i][2]) > 0:
            count += one[num - 2 * int(arr[i][2])]
            three_1[num - 2 * int(arr[i][2])] += 1
        three[num] += 1
    elif len(arr[i]) == 4:
        num = int(arr[i][0]) + int(arr[i][1]) + int(arr[i][2]) + int(arr[i][3])
        count +=  2 * four[num]
        if num - 2 * (int(arr[i][0])) > 0:
            count += two[num - 2 * (int(arr[i][0]))]
            four_2[num - 2 * (int(arr[i][0]))] += 1
        if num - 2 * (int(arr[i][3])) > 0:
            count += two[num - 2 * (int(arr[i][3]))]
            four_2[num - 2 * (int(arr[i][3]))] += 1
        four[num] += 1
    elif len(arr[i]) == 5:
        num = int(arr[i][0]) + int(arr[i][1]) + int(arr[i][2]) + int(arr[i][3]) + int(arr[i][4])
        count += 2 * five[num]
        if num - 2 * (int(arr[i][0]) + int(arr[i][1])) > 0:
            count += one[num - 2 * (int(arr[i][0]) + int(arr[i][1]))]
            five_2[num - 2 * (int(arr[i][0]) + int(arr[i][1]))] += 1
        if num - 2 * (int(arr[i][0])) > 0:
            count += three[num - 2 * (int(arr[i][0]))]
            five_1[num - 2 * (int(arr[i][0]))] += 1
        if num - 2 * (int(arr[i][3]) + int(arr[i][4])) > 0:
            count += one[num - 2 * (int(arr[i][3]) + int(arr[i][4]))]
            five_2[num - 2 * (int(arr[i][3]) + int(arr[i][4]))] += 1
        if num - 2 * (int(arr[i][4])) > 0:
            count += three[num - 2 * (int(arr[i][4]))]
            five_1[num - 2 * (int(arr[i][4]))] += 1

        five[num] += 1
    # print(count)
print(count)