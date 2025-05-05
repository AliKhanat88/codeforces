def sol():
    # print("new test")
    a, b = input().split()
    i = 0
    j = len(a) - len(b)
    sumi = 0
    while i < len(b):
        if j < 0:
            sumi += int(b[i])
            break
        elif a[j] != b[i]:
            sumi += abs(int(a[j]) - int(b[i]))
            break
        # print(sumi, i, j)
        i += 1
        j += 1
    
    if (len(b) - i -1) * 9 > 0:
        sumi += (len(b) - i -1) * 9
    print(sumi)
for t in range(int(input())):
    sol()