def check_doable(n, k, arr):
    per = 99999999999
    for i in range(k-1, 0, -1):
        cur = arr[i] - arr[i-1]
        if per < cur:
            print("NO")
            return
        per = cur
    if (n-k+1) * per >= arr[0]:
        print("YES")
    else:
        print("NO")

def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        check_doable(n, k, arr)

main()