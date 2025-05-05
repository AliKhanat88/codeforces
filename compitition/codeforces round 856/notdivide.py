def not_divisible(n, arr):
    for i in range(n):
        arr[i] += 1
    for i in range(1, n):
        if arr[i] % arr[i-1] == 0:
            arr[i] += 1
    print(" ".join(list(map(str, arr))))


def main():
    for i in range(int(input())):
        n = int(input())
        arr= list(map(int, input().split()))
        not_divisible(n, arr)

main()