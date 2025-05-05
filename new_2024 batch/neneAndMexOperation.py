def recur(l, r, ans=[]):
    if r - l == 0:
        ans.append((l, r))
    elif r - l < 0:
        return
    else:
        recur(l, r - 1, ans)
        ans.append((l, r))
        recur(l, r - 1, ans)
# temp = []
# recur(1, 3, temp)
# print(temp)
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print("TEST")
    maxi_val = None
    maxi = -1
    for i in range((2 ** (n))):
        per = -1
        temp = 0
        for j in range(n):
            if i & (2**j) != 0:
                # print(j - per - 1)

                temp += arr[j]
                temp += (j - per - 1) * (j - per - 1)
                per = j
        temp += (n-1 - per) * (n-1 - per)
        # print(bin(i), temp)
        if temp > maxi:
            maxi_val = i
            maxi = temp
    
    # print(maxi, bin(maxi_val))
    
    ans = []
    for i in range(n):
        if maxi_val & (2**i) == 0:
            if arr[i] != 0:
                ans.append((i+1, i+1))
    per = -1
    for i in range(n):
        if maxi_val & (2**i) != 0:
            if i - per > 1:
                temp = [(per+2, per+2)]
                recur(per+2, i, temp)
                temp.append((per+2, i))
                ans += temp
                per = i
            else:
                per = i
    
    if per != n-1:
        temp = [(per+2, per+2)]
        recur(per +2, n, temp)
        # print(bin(maxi_val))
        temp.append((per+2, n))
        ans += temp

    print(maxi, len(ans))
    for temp in ans:
        print(temp[0], temp[1])
# for t in range(int(input())):
solve()