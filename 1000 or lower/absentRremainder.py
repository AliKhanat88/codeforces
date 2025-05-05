def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        mini = min(arr)
        arr.remove(mini)
        for i in range(n//2):
            print(arr[i], mini)

main()