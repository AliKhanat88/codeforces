from math import comb

rem = 998244353
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    for i in range(2, n, 3):
        temp = [arr[i], arr[i-1], arr[i-2]]
        temp.sort()
        if len(set(temp)) == 1:
            ans = (ans * 3) % rem
        elif len(set(temp)) == 2:
            if temp[0] == temp[1]:
                ans = (ans * 2) % rem
    factorial = [1] * (n // 3 + 1)

    for i in range(2, n//3+1):
        factorial[i] = (factorial[i-1] * i) % rem

    # print(factorial)

    temp = factorial[n // 3] * pow(factorial[n // 6], rem - 2, rem) * pow(factorial[n // 3 - n // 6], rem - 2, rem)

    
    print((ans * temp) % 998244353)

    

    return (ans * temp) % 998244353

if __name__ == "__main__":

    solve()