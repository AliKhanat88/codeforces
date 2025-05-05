def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print((n - 1) // 2)
    for i in range(0, n-1, 2):
        print(arr[i+1], arr[i], end=" ")
    if n %2 == 1:
        print(arr[-1])
    else:
        print()
main()