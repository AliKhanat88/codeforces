def print_ways(n, arr):
    arr.sort()
    count = 0
    for i in range(n-1):
        if arr[i] > i or arr[i+1] <= i + 1:
            continue
        count+=1
    if arr[0] != 0:
        count += 1
    print(count+1)
    

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        print_ways(n, arr)

main()