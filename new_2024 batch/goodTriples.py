def solve():
    num = int(input())
    cur_sum = 1
    while num > 0:
        temp = num % 10
        num = num // 10
        new_sum = 0
        for i in range(1, temp + 2):
            new_sum += i * cur_sum
        cur_sum = new_sum
    print(cur_sum)

for t in range(int(input())):
    solve()