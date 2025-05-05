def print_max_min(n, arr):
    arr.sort()
    maxi = arr[0]
    diff = arr[0]
    for i in range(1, n):
        temp = arr[i] - diff
        if temp > maxi:
            maxi = temp
        diff += temp
    print(maxi)



def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print_max_min(n, arr)

main()