def checkDoable(n, arr):
    if arr[0] == n:
        print(n, end=" ")
        for i in range(n-1, 0, -1):
            print(arr[i], end=" ")
        print()
    elif arr[-1] == n:
        print(n, end=" ")
        for i in range(n-2, -1, -1):
            print(arr[i], end=" ")
        print()
    else:
        print(-1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        checkDoable(n, arr)

main()