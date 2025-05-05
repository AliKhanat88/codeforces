def print_comb(n):
    start_sum = 2 * n + 1 - n // 2
    for i in range(1, n +1, 2):
        print(i, start_sum-i)
        start_sum += 1
    for i in range(2, n+1, 2):
        print(i, start_sum-i)
        start_sum += 1


for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        print_comb(n)