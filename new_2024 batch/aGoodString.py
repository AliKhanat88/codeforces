def recur(s, i, j, char):
    # print(i, j, char)
    if j - i == 0:
        if s[i] == char:
            return 0
        else:
            return 1
    else:
        mid = i + (j - i + 1) // 2
        count1 = 0
        count2 = 0
        for k in range(i,mid):
            if s[k] != char:
                count1 += 1
        for k in range(mid, j+1):
            if s[k] != char:
                count2 += 1
        return min(count2+recur(s, i,mid-1, chr(ord(char)+1)), count1+recur(s, mid,j,chr(ord(char)+1)))

def solve():
    n = int(input())
    s = input()
    # print("TEST------")
    # print(s)
    print(recur(s, 0, len(s)-1, "a"))


for t in range(int(input())):
    solve()