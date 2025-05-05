from math import ceil
def print_equalize(n, arr):
    arr = sorted(arr, key=lambda x: x[1])
    r = ""
    count = 0
    for i in range(1, n):
        if arr[i][1] == 1 or arr[i-1][1] == 1:
            print(-1)
            break
        else:
            is_two = False
            while arr[i][1] != arr[i-1][1]:
                if arr[i][1] == 2:
                    index = i
                    is_two = True
                    break
                elif arr[i-1][1] == 2:
                    index = i-1
                    is_two = True
                    break
                arr[i][1] = ceil(arr[i][1] / arr[i-1][1])
                r += f"{arr[i][0] + 1} {arr[i-1][0] + 1}\n"
                count += 1
                if arr[i-1][1] > arr[i][1]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
        if is_two == True:
            break
    if is_two == True:
        for i in range(n):
            if arr[i][1] == 1:
                print(-1)
                return
            elif arr[i][1] == 2:
                continue
            elif index != i:
                arr[i] == ceil(arr[i] / 2)
                count += 1
                r += f"{arr[i][0] + 1} {arr[index][0] + 1}\n"
                
    print(count)
    print(r[:-1])

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        pair_arr = [[i, arr[i]] for i in range(n)]
        print_equalize(n, pair_arr)

main()