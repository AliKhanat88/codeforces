x = 5
m = 10000
count = 0
for i in range(1, m + 1):
    if (i ^ x) % x == 0 or (i ^ x) % i == 0:
        count += 1
print(count)