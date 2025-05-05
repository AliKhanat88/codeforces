def get_divisors(num):
    arr = []

    i = 2
    while i <= num:
        if num % i == 0:
            arr.append(i)
        i += 1

    return arr

# print(bin_check(100, 1233, 2))
def solve():
    a, b = map(int, input().split())

    # ans_set = []
    print(a, b)
    i = 2 
    ans = 0
    while i <= b:
        arr = get_divisors(i)
        print(arr, i)
        for num in arr:
            if num * num - i <= a:
                print(i, num * num - i)
                ans += 1
        i += 1

    print(ans)

for t in range(int(input())):
    solve()
# a = 20
# b = 20
# count = 0
# for i in range(1, b+1):
#     for j in range(1, a + 1):
#         if (i * gcd(i, j)) % (i + j) == 0:
#             if i + j == 25:
#                 print(i , j)
# print(count)