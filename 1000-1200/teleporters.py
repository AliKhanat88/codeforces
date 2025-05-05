def print_max_tele(n, c, arr):
    arr = sorted(arr)
    count = 0
    for i in range(n):
        if arr[i] <= c:
            count += 1
            c = c - arr[i]
        else:
            break
    print(count)

def main():
    t = int(input())
    for i in range(t):
        n, c = map(int, input().split())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i]) + i+1
        print_max_tele(n, c, arr)

main()