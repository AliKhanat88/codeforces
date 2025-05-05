def elimination(n, arr):
    is_pattern = True
    for i in range(n-2):
        if arr[i] != arr[i+2]:
            is_pattern = False
            break
    if is_pattern == True:
        print(n // 2 + 1)
    else:
        print(n)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        elimination(n, arr)
main()