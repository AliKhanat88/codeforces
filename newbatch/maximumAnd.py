import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    a_list = [arr]
    b_list = [brr]
    ans = 0
    for b in range(30, -1, -1):
        new_a_list = []
        new_b_list = []
        done = True
        for i in range(len(a_list)):
            temp_a_1 = []
            temp_b_1 = []
            temp_a_0 = []
            temp_b_0 = []
            for j in range(len(a_list[i])):
                if a_list[i][j] & (2 ** b) != 0:
                    temp_a_1.append(a_list[i][j])
                else:
                    temp_a_0.append(a_list[i][j])
                if b_list[i][j] & (2 ** b) != 0:
                    temp_b_1.append(b_list[i][j])
                else:
                    temp_b_0.append(b_list[i][j])
            if len(temp_a_1) == len(temp_b_0) and len(temp_a_0) == len(temp_b_1):
                if len(temp_a_1) != 0:
                    new_a_list.append(temp_a_1)
                    new_b_list.append(temp_b_0)
                if len(temp_b_1) != 0:
                    new_a_list.append(temp_a_0)
                    new_b_list.append(temp_b_1)
            else:
                done = False
                break
        if done:
            ans += (2 ** b)
            a_list = new_a_list
            b_list = new_b_list
    print(ans)
for t in range(int(input())):
    solve()