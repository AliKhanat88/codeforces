def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    count_arr = [0] * (n +1)
    for num in arr:
        count_arr[num] += 1
    
    


    print(count)
        
for t in range(int(input())):
    solve()