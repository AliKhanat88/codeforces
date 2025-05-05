def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        if n > k:
            print("NO")
            continue
        if n % 2 == 0 and k % 2 == 1:
            print("NO")
            continue
        else:
            print("YES")
            if n % 2 == 1:
                for i in range(n-1):
                    k -= 1
                    print(f"1", end=" ")
                print(k)
            elif n == k:
                for i in range(n):
                    print("1", end = " ")
                print()
            else:
                while n > 2:
                    k -= 1
                    n -= 1
                    print(f"1", end= " ")
                print(f"{(k) // 2} {(k) // 2}")

main()