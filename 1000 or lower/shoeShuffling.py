from collections import defaultdict

def print_combination(n, arr):
    count_list = defaultdict(lambda: 0)
    for i in range(n):
        arr[i] = int(arr[i])
        count_list[arr[i]] += 1
    mini = min(count_list.values())
    if mini <= 1:
        print(-1, end="")
    else:
        k = 1
        for value in count_list.values():
            print(k + value - 1, end=" ")
            for j in range(value-1):
                print(k + j, end = " ")
            k += value

    print()


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        print_combination(n, arr)

main()