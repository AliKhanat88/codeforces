import sys
input = sys.stdin.readline

dict = {
    0: -1,
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
    "E": 10000
}

def solve():
    s = input()
    ans = 0
    left_big = [0] * (len(s))
    per = s[-1]
    ans += dict[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        left_big[i] = per
        if dict[s[i]] < dict[left_big[i]]:
            ans = ans - dict[s[i]]
        else:
            ans = ans + dict[s[i]]
        if dict[per] < dict[s[i]]:
            per = s[i]

    count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0
    }
    maxi = ans
    for i in range(len(s)):
        temp_sum = ans
        if left_big[i] == 0:
            left_big_i = "A"
        else:
            left_big_i = left_big[i]
        if dict[s[i]] < dict[left_big_i]:
            temp_sum += dict[s[i]]
        else:
            temp_sum -= dict[s[i]]
        for j in range(ord(left_big_i), ord(s[i])):
            temp_sum += ((count[chr(j)] * dict[chr(j)]) * 2)


        for j in range(ord("A"), ord("E") + 1):
            temp_sum2 = temp_sum
            char = chr(j)
            if dict[char] < dict[left_big_i]:
                temp_sum2 -= dict[char]
            else:
                temp_sum2 += dict[char]

            for k in range(ord(left_big_i), ord(char)):
                temp_sum2 = temp_sum2 - ((count[chr(k)] * dict[chr(k)]) * 2)
            maxi = max(maxi, temp_sum2)
        count[s[i]] += 1
        for k in range(ord("A"), ord(s[i])):
            count[chr(k)] = 0
    print(maxi)
            

    # print(ans)
    # print(left_big)



for t in range(int(input())):
    solve()