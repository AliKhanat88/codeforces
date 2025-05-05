def print_val(length, comb):
    comparer = "1"
    count = 0
    for i in range(length):
        if comb[i] == comparer:
            count += 1
            if comparer == "0":
                comparer = "1"
            else:
                comparer = "0"
    if count == 0:
        print(0)
    else:
        print(count-1)



def main():
    n = int(input())
    for i in range(n):
        length = int(input())
        comb = input().rstrip()
        print_val(length, comb)
main()