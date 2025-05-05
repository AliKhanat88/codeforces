from math import ceil
def print_pigs(n, arr):
    used = 0
    min_used = 0
    cur = 0
    total = 0
    for i in range(n):
        if arr[i] == "2":
            used = max(min_used + cur, used)
            total = total + cur
            if total != 0:
                min_used = ceil((total - 1) / 2 + 1)
            else:
                min_used = 0
            cur = 0
        elif i == n -1:
            cur += 1
            used = max(min_used + cur, used)
            total = total + cur
            if total != 0:
                min_used = ceil((total - 1) / 2 + 1)
            else:
                min_used = 0
            cur = 0
        elif arr[i] == "1":
            cur += 1
    print(used)
def main():
    for i in range(int(input())):
        n = int(input())
        arr = input().split()
        print_pigs(n, arr)
main()
