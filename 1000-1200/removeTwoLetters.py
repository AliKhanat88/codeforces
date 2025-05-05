def main():
    for i in range(int(input())):
        n = int(input())
        s= input()
        first = s[:2]
        total = 1
        for j in range(1, n-1):
            temp = s[j+1:j-1:-1]
            if first != temp:
                total += 1
            first = s[j:j+2]
        print(total)
main()