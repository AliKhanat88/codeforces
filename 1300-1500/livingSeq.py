from math import comb
from collections import defaultdict

dict = defaultdict(lambda: -1)
def check_4(num):
    count = 0
    
    if int(num[0]) >= 4:
        count += 9 ** (len(num) - 1)
        product = int(num[0])
        for i in range(1, len(num)):
            count += product * 9 ** (len(num) - 1 - i) * comb(len(num) - 1, i)
            count += 9 ** (len(num) - 1 - i) * comb(len(num) - 1, i)
    else:
        product = int(num[0]) + 1
        for i in range(1, len(num)):
            count += product * 9 ** (len(num) - 1 - i) * comb(len(num) - 1, i)

    return count




def solve():
    n = int(input())
    per_count = 0
    temp = n
    while True:
        count = 0
        while len(str(temp)) != 1:
            rem = temp % 10**(len(str(temp)) -1) + 1
            if dict[(len(str(temp)), str(temp)[0])] == -1:
                dict[(len(str(temp)), str(temp)[0])] = check_4(str(temp - rem))
            count += dict[(len(str(temp)), str(temp)[0])]
            # print(count, temp, rem)
            if str(temp - rem)[0] == "3":
                count += rem
                temp = 0
                break
            
            temp = rem - 1
        if temp >= 4:
            count += 1
        
        if count - per_count == 0:
            break
        temp = n + count
        per_count = count 
        # print(count, temp)
    print(n + count)

        
    
    

for t in range(int(input())):
    solve()