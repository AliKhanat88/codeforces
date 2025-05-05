for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    odd_sum = 0
    even_sum = 0
    for j in range(n):
        if arr[j] % 2 == 0:
            even_sum += arr[j]
        else:
            odd_sum += arr[j]
    if even_sum > odd_sum:
        print("YES")
    else:
        print("NO")
        
