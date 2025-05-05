def check_doable(n, arr):
    for i in range(1, n):
        if arr[i-1] - arr[i] >= 0 and arr[i-1] != 0 and arr[i] != 0:
            print(-1)
            return
        else:
            arr[i] = arr[i] + arr[i-1]

    print(" ".join(list(map(str, arr))))

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        check_doable(n, arr)

main()