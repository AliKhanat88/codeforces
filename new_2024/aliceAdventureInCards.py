def solve():
    n = int(input())
    q = list(map(int, input().split()))
    k = list(map(int, input().split()))
    j = list(map(int, input().split()))

    mini_q_ind = n - 1
    mini_j_ind = n - 1
    mini_k_ind = n - 1
    ans = [-1] * n

    for i in range(n-2, -1, -1):
        if q[i] > q[mini_q_ind]:
            ans[i] = ("q", mini_q_ind)
            if k[mini_k_ind] > k[i]:
                mini_k_ind = i
            if j[mini_j_ind] > j[i]:
                mini_j_ind = i
        if k[i] > k[mini_k_ind]:
            ans[i] = ("k", mini_k_ind)
            if q[mini_q_ind] > q[i]:
                mini_q_ind = i
            if j[mini_j_ind] > j[i]:
                mini_j_ind = i
        if j[i] > j[mini_j_ind]:
            ans[i] = ("j", mini_j_ind)
            if q[mini_q_ind] > q[i]:
                mini_q_ind = i
            if k[mini_k_ind] > k[i]:
                mini_k_ind = i
    # print(ans)
    if ans[0] == -1:
        print("NO")
        return
    print("YES")
    temp_ans = []
    temp = ans[0]
    while temp[1] != n - 1:
        temp_ans.append(f"{temp[0]} {temp[1] + 1}")
        temp = ans[temp[1]]
    temp_ans.append(f"{temp[0]} {temp[1] + 1}")
    print(len(temp_ans))
    print("\n".join(temp_ans))

for t in range(int(input())):
    solve()