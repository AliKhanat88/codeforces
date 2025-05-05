def print_permute(n, k):
    pos_neg = [False] * n
    i = n
    while i > 0:
        if k - i >= 0:
            pos_neg[i-1] = True
            k -= i
        i -= 1
    # print(pos_neg)
    # pos_neg = [False, False, False, True, True, False, True, True, True, False]
    arr = [0] * n
    i = 0
    per_neg = 0
    per_pos = 0
    while i < n:
        if pos_neg[i] == True:
            arr[i] = abs(per_neg) + 1
            per_pos = arr[i]
            j = i + 1
            while j < n and pos_neg[j] == True:
                arr[j] = 1
                j += 1
                per_pos += 1
            i = j - 1
        else:
            arr[i] = -(per_pos + 1)
            per_neg = arr[i]
            j = i + 1
            while j < n and pos_neg[j] == False:
                arr[j] = -1
                j += 1
                per_neg -= 1
            i = j - 1
        i += 1
    print(" ".join(map(str, reversed(arr))))
def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        print_permute(n, k)

main()
