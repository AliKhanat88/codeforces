def main():
    a = [i for i in range(10**5)]
    for i in range(2, 10**5 // 2):
        for j in range(i+i, 10**5, i):
            a[j] = -1
    a[0] = -1
    a[1] = -1
    n = int(input())
    for i in range(n):
        x = int(input())
        j = 2
        while a[j] != -1 and a[x + a[j]] != -1:
            j = j + 1
        print(a[j])
            
        

main()
