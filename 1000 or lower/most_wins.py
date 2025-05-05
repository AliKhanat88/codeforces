from math import floor

def main():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    diff = floor(d / arr[0]) + 1
    count = 0
    i = 1
    length = n
    while n >= diff:
        count += 1
        n = n - diff
        if i < length:
            diff = floor(d / arr[i]) + 1
            i += 1
        else:
            break
    print(count)
main()