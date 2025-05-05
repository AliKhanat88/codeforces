def solve():
    s = input()
    per = 1
    count = 0
    for i in range(len(s)):
        if s[i] == "0":
            temp = 10
        else:
            temp = int(s[i])
        count += abs(temp - per)
        per = temp
    print(count + 4)



for t in range(int(input())):
    solve()