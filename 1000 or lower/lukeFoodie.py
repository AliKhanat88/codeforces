def print_food_diff(n, x, arr):
    if n == 1:
        print(0)
        return
    count = 0
    maxi = arr[0]
    mini = arr[0]
    for i in range(1, n):
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]
        if maxi - mini > (2 * x):
            count += 1
            maxi = arr[i]
            mini = arr[i]
    print(count)

def main():
    t = int(input())
    for i in range(t):
        n , x = map(int, input().split())
        arr = list(map(int, input().split()))
        print_food_diff(n, x, arr)

main()