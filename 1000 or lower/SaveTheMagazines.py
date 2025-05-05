def print_mag(length, lids, magazines):
    sum = 0
    last_zero = -1
    min = 1000000000
    for i in range(length+1):
        if i == length or lids[i] == 0:
            if last_zero != -1 and last_zero != i - 1:
                if magazines[last_zero] > min:
                    sum += magazines[last_zero]
                    sum -= min
            last_zero = i
            min = 100000000
        elif lids[i] == 1:
            if min > magazines[i]:
                min = magazines[i]
            sum += magazines[i]
            
    print(sum)


def main():
    t = int(input())
    for i in range(t):
        length = int(input())
        lids = [int(num) for num in input()]
        magazines = [int(num) for num in input().split()]
        print_mag(length, lids, magazines)

main()