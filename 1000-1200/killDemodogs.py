def main():
    for i in range(int(input())):
        n = int(input())
        n = n - 1
        result1 = n * (n+1) * (2 * n + 1) // 6
        result2 = n * (n + 1) // 2
        result = result1 * 2 + result2 + (n+1)**2
        print((result * 2022) % 1000000007)

main()
            