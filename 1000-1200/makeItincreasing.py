n= int(input())
arr = list(map(int, input().split()))
mini = 9999999999999999999999999999999999999999999
for i in range(n):
    count = 0
    per = 0
    for j in range(i-1, -1, -1):
        temp = per // arr[j] + 1
        count += temp 
        per = temp * arr[j]
    per = 0
    for j in range(i+1, n):
        temp = per // arr[j] + 1
        count += temp 
        per = temp * arr[j]
    mini = min(count, mini)

print(mini)