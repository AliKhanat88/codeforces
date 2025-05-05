def check_game(n, arr):
    if n % 2 == 1:
        print("Mike")
        return
    index = 0
    mini = 9999999999
    for i in range(n):
        if arr[i] < mini:
            mini = arr[i]
            index = i
    if index % 2 == 0:
        print("Joe")
    else:
        print("Mike")

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        check_game(n, arr)


main()