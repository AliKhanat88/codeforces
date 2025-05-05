

# def solve(n, k, arr, brr):
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    lrr = [(brr[i] - arr[i] + 1, i) for i in range(n)]
    # print(arr)
    # print(brr)


    sumi = 0
    j = 0
    count = 0
    ones = 0
    while j < n:
        if sumi >= k:
            break
        if lrr[j][0] == 1:
            ones += 1
        sumi += lrr[j][0]
        count += 1
        j += 1
    if sumi < k and j >= n:
        print(-1)
        return -1
    j -= 1
    mini = brr[j] - (sumi - k) + 2 * count
    # print(mini)
    # print(sumi)
    if ones >= (sumi - k):
        ones -= (sumi - k)
        count = count - (sumi - k)
        mini = min(mini, brr[j] + count * 2)
    else:
        count -= ones
        mini = min(mini, arr[j] + lrr[j][0] - (sumi - k) - 1 + ones + 2 * count)
        ones = 0
    # print(j)
    # print(ones)
    # print(lrr)
    # print(count)
    # print(mini)
    for i in range(j + 1, n):
        if ones == 0:
            break
        if lrr[i][0] == 1:
            pass
        elif lrr[i][0] <= ones:
            ones -= lrr[i][0]
            count = count - lrr[i][0] + 1

            mini = min(mini, count * 2 + brr[i])
        else:
            count = count - ones + 1
            mini = min(mini, arr[i] + ones - 1 + 2 * count)
            ones = 0
        # print(ones)
    print(mini)
    return mini

        
if __name__ == "__main__":
    for t in range(int(input())):
        solve()