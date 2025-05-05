n = int(input())
s = input()

low = 1
high = 2**n
low_i = 0
high_i = 0
for i in range(n):
    if s[i] == '0':
        high -= (2 ** high_i)
        high_i += 1
    else:
        low += (2**low_i)
        low_i += 1
for i in range(low, high + 1, 1):
    print(i, end=" ")
print()
