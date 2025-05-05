ans = 0
mul = 2
for i in range(7, 0, -1):
    for j in range(i):
        ans = ans + j * mul
    mul = mul * 2
print(ans * 2)