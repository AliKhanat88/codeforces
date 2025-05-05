def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        for j in range(1, n//2+1):
            print(f"{n+1-j} {j} ", end="")
        if n % 2 == 1:
            print((n+1) //2 , end="")
        print()
main()
