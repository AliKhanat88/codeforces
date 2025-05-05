from math import ceil, floor

def main():
    for t in range(int(input())):
        n = int(input())
        if n % 2 == 0:
            print(-1)
            continue
        else:
            r = ""
            m = 0
            while n > 1:
                temp1 = ceil(n // 2)
                temp2 = floor(n//2)
                if temp1 % 2 == 1:
                    r = "2 " + r
                    n = temp1
                else:
                    r = "1 " + r
                    n = temp2
                m += 1
            print(m)
            print(r)

main()
