import sys
input = sys.stdin.readline
from math import lcm

def solve():
    n = int(input())
    arr = [1] * n
    a_arr = [0] * n
    b_arr = [0] * n
    per = 0
    ans = 1
    for i in range(n):
        a,b = map(int, input().split())
        a_arr[i] = a
        b_arr[i] = b

    done = True
    for i in range(1, n):
        if done == False:
            arr[i-1] = 1
        done = True
        print(arr, ans, per)
        for j in range(i, per, -1):
            temp = lcm(b_arr[j-1], b_arr[j])
            arr[j] = lcm(temp // b_arr[j], arr[j])
            if temp // b_arr[j-1] == arr[j-1]:
                print(1)
                break
            elif temp // b_arr[j-1] < arr[j-1]:
                print(2)
                if a_arr[j] % (lcm(arr[j-1], temp // b_arr[j-1]) // (temp // b_arr[j-1]) * arr[j]) == 0:
                    break
                else:
                    per = i
                    ans += 1
                    done = False
                    break
            else:
                print(3)
                arr[j-1] = lcm(temp // b_arr[j-1], arr[j-1])
                if a_arr[j] % arr[j] != 0:
                    per = i
                    ans += 1
                    done = False
                    break
        if done:
            if a_arr[per] % (arr[per]) != 0:
                per = per + 1
                ans += 1
                done = False
        
    print(ans)
        
for t in range(int(input())):
    solve()