from math import log2
n = int(input())
arr = list(map(int, input().split()))
VAR = 32768
for num in arr:
    mini = 9999999999999999999999999999999999
    operation = 0
    while True:
        if num % VAR == 0:
            diff = 0
        else:
            diff = VAR - (num % VAR)
        add_step = diff // (2 ** operation)
        remain = diff - add_step * (2 ** operation)
        operations = remain + add_step + operation
        if operation < mini:
            num = num * 2
            operation += 1
        else:
            break
        if operations < mini:
            mini = operations
    print(mini, end=" ")
