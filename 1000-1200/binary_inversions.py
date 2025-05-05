def max_inversions(n, arr):
    zeros = 0
    inversions = 0
    total_0 = 0
    total_1 = 0
    for i in range(n-1, -1, -1):
        if arr[i] == 0:
            zeros += 1
            total_0 += 1
        elif arr[i] == 1:
            total_1 += 1
            inversions += zeros
    # print(inversions)

    last_1_zero = 0
    for i in range(n-1, -1,-1):
        if arr[i] == 1:
            break
        last_1_zero += 1

    first_zero_1 = 0
    for i in range(n):
        if arr[i] == 0:
            break
        first_zero_1 += 1
    
    print(max(total_0 - 1 - first_zero_1 + inversions, total_1 - 1 - last_1_zero + inversions, inversions))



def main():
    for i in range(int(input())):
        n  = int(input())
        arr = list(map(int, input().split()))
        if n == 1:
            print(0)
        else:
            max_inversions(n, arr)

main()
                   