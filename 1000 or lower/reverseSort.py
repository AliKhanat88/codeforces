def print_number_of_cases(n, arr):
    indexes = []
    last = n-1
    i = 0
    while i <= last:
        if arr[i] == "1":
            for j in range(last, i, -1):
                last -= 1
                if arr[j] == "0":
                    indexes.append(i+1)
                    indexes.append(j+1)
                    break
        i += 1
    indexes.sort()
    if len(indexes) == 0:
        print(0)
    else:
        print(1)
        print(len(indexes), *indexes)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input()
        print_number_of_cases(n, arr)

main()