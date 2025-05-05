from collections import defaultdict
def print_min_lexo(n, arr):
    i = n-1
    while i > 0:
        if arr[i] < arr[i-1]:
            mini = arr[i]
            break
        i = i - 1
    for j in range(i-1, -1, -1):
        if arr[j] <= mini:
            mini = arr[j]
        else:
            if arr[j] > 7:
                arr[j] = 9
            else:
                arr[j] += 1
    dict = defaultdict(lambda:0)

    for i in range(n):
        dict[arr[i]] += 1
        
    for i in range(10):
        for j in range(dict[i]):
            print(f"{i}", end="")
    print()
def main():
    for i in range(int(input())):
        s = input()
        n = len(s)
        arr = [int(s[i]) for i in range(n)]
        print_min_lexo(n, arr)
main()
