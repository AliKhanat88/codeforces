from collections import defaultdict

def print_min_ope(n, s, arr):
    arr_sum = [0] * n
    arr_sum[0] = arr[0]
    for i in range(1, n):
        arr_sum[i] = arr_sum[i-1] + arr[i]
    forward_dict = defaultdict(lambda:-1)
    for i in range(n):
        forward_dict[arr_sum[i]] = i + 1
    backword_dict = defaultdict(lambda:-1)
    for i in range(n-1, -1, -1):
        backword_dict[arr_sum[i]] = i + 1
    if forward_dict[0] == -1:
        forward_dict[0] = 0
    backword_dict[0] = 0
    mini = 9999999999999999999999
    k = s
    while k <= arr_sum[-1]:
        mini = min(n - forward_dict[k] + backword_dict[k-s], mini)
        k += 1
    if mini == 9999999999999999999999:
        print(-1)
    else:
        print(mini)


for t in range(int(input())):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print_min_ope(n, s, arr)