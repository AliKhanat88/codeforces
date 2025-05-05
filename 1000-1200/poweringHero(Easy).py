def print_hero(n, arr):
    cost = 0
    i = 0
    while i < n:
        if arr[i] == 0:
            count = 1
            i = i + 1
            while i < n and arr[i] == 0:
                count += 1
                i += 1
            arr[:(i-count)] = sorted(arr[:(i-count)], reverse=True)
            j = 0
            while count > 0 and j < i - count:
                cost += arr[j]
                arr[j] = 0
                count -= 1
                j += 1
        else:
            i += 1
    print(cost)
 
def main():
    for i in range(int(input())):
        n = int(input())
        arr= list(map(int, input().split()))
        print_hero(n, arr)
 
main()