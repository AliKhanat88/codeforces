def print_num(n, d, num):
    num = list(num)
    for i in range(n):
        if int(num[i]) < int(d):
            temp = num[:i] + [d] + num[i:]
            print("".join(temp))
            return
    temp = num + [d]
    print("".join(temp))

for t in range(int(input())):
    n, d = input().split()
    n = int(n)
    num = input()
    print_num(n, d, num)
        
