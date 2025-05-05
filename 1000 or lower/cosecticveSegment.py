def is_consective(n, arr):
    if n == 1:
        print("YES")
        return
    possible = 3
    diff = 0
    for i in range(1, n):
        diff += arr[i] - arr[i-1]
        if diff > possible:
            print("NO")
            return
        possible += 1

    print("YES")
    


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        is_consective(n, arr)

main()