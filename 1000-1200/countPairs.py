from collections import defaultdict
def print_max_pair(n, k, arr):
    pairs = 0
    for i in range(ord("A"), ord("Z") + 1):
        cm = chr(i+32)
        sm = chr(i)
        if arr[cm] > arr[sm]:
            mini = arr[sm]
            arr[cm] -= mini
            arr[sm] -= mini
            if 2 * k <= arr[cm]:
                pairs += k
                k -= k
            else:
                pairs += arr[cm] // 2
                k -= arr[cm] // 2
        elif arr[sm] > arr[cm]:
            mini = arr[cm]
            arr[cm] -= mini
            arr[sm] -= mini
            if 2 * k <= arr[sm]:
                pairs += k
                k -= k
            else:
                pairs += arr[sm] // 2
                k -= arr[sm] // 2
        else:
            mini = arr[sm]
            arr[cm] -= mini
            arr[sm] -= mini
        pairs += mini
    print(pairs)

def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        arr = defaultdict(lambda: 0)
        for chr in s:
            arr[chr] += 1
        print_max_pair(n, k, arr)

main()