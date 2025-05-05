for t in range(int(input())):
    n = int(input())
    sumi = 0
    j = n
    for i in range(n):
        sumi += abs(j - (i+1))
        j -= 1
    print(sumi // 2 + 1)
