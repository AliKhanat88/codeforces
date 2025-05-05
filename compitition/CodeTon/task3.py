def min_cost(n, r, a, arr):
    new_n = len(arr)
    cost = (n - new_n) * r
    arr.sort()
    if arr[0] != 1:
        cost += a
        arr = [1] + arr
        new_n += 1
    mini = 9999999999999999999999999999999999999
    pre_rem = 0
    for i in range(1, new_n):
        add = (arr[-1] - (new_n - i) - arr[i-1]) * a
        rem = (new_n - i) * r
        mini = min(add + pre_rem,rem + pre_rem,mini)
        pre_rem += (arr[i]-arr[i-1] - 1) * a
    if mini == 9999999999999999999999999999999999999:
        print(cost)
    else:
        print(cost + mini)

def main():
    for t in range(int(input())):
        n, r, a = map(int, input().split())
        arr = list(set(map(int, input().split())))
        min_cost(n, r, a, arr)

main()