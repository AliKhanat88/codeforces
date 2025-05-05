def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    maxi = 0
    maxi_first = 0

    cur_first = 0
    i = 0
    sumi = 0
    while i < n:
        if arr[i] < 0:
            j = i + 1
            min_neg = arr[i]
            cur_sumi = arr[i]
            sumi += arr[i]
            while j < n:
                if sumi + arr[j] > cur_first:
                    sumi += arr[j]
                    break
                cur_sumi += arr[j]
                sumi += arr[j]
                min_neg = min(cur_sumi, min_neg)
                j += 1
            # print(min_neg, cur_first, sumi)
            if min_neg < maxi:
                maxi = min_neg
                maxi_first = cur_first
                cur_first = sumi
            else:
                cur_first = sumi
            i = j
        else:
            sumi += arr[i]
            cur_first = sumi
        # print(sumi)
        i += 1
    print(maxi_first)
    # return maxi_first

if __name__ == "__main__":
    for t in range(int(input())):
        solve()