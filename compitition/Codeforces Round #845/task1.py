def print_non_same_partial(n, arr):
    count = 0
    for i in range(1, n):
        if arr[i-1] % 2 == arr[i] % 2:
            count+=1

    print(count)




def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        print_non_same_partial(n, arr)

main()