

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    per = 0
    # print(arr)
    ans = []
    for i in range(n-1):
        per = per ^ arr[i]
        ans.append(per) 
    temp = 0
    for b in range(20, -1, -1):
        count = 0
        for i in range(n-1):
            if ans[i] & (2 ** b) != 0:
                count += 1
        if count > n / 2:
            temp = temp + (2 ** b)
    print(temp, end = " ")
    for i in range(n-1):
        print(ans[i] ^ temp, end=" ")

    

solve()