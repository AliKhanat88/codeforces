from math import log2

def find_min(num, power):
    count = 0
    for i in range(power, 0, -1):
        if num - i >= 0:
            num = num - i
            count += 1
            if num == 0:
                break
    return count


def print_min(n, product):
    if product % (2 **n) == 0:
        print(0)
        return
    power = int(log2(n))
    max_power = int((power * (power + 1)) / 2)
    mini = 99999999
    for i in range(n-max_power, n):
        if product % (2**i) == 0:
            temp = find_min(n-i, power)
            if temp < mini:
                mini = temp
    if mini != 99999999:
        print(mini)
    else:
        print(-1)


def main():
    for i in range(int(input())):
        n = int(input())
        product = 1
        arr = input().split()
        for num in arr:
            product = product * int(num)
        print_min(n, product)
main()