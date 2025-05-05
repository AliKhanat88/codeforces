def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    mini = min(arr)
    mini = mini - 1
    lacking = mini * k
    lacking += n - sum(arr) 
    print(lacking)

main()