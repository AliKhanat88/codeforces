def check_min_diff(higher, n, num):
    min_diff = float("inf")
    i = 0
    for number in higher:
        if abs(number - num) < min_diff:
            min_diff = abs(number - num)
            index = i
        i = i + 1
    number = higher.pop(index)
    return number


def print_permutation(n, arr, recommended):
    count = 0
    for bit in recommended:
        if bit == "1":
            count += 1
    higher = n - count
    higher_nums = [i for i in range(higher+1, n+1)]
    lower_nums = [i for i in range(1, higher+1)]
    for j in range(n):
        if recommended[j] == "0":
            print(check_min_diff(lower_nums,n, arr[j]), end=" ")
        else:
            print(check_min_diff(higher_nums,n, arr[j]), end=" ")
    print()

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(num) for num in input().split()]
        recommended = input()
        print_permutation(n, arr, recommended)

main()