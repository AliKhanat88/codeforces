def print_permute(n, arr):
    i = 0 
    s = ""
    while i < n:
        if arr[i] != 1:
            break
        s += "1 "
        i = i + 1
    previous = 1
    product = 1
    count = 1
    for i in range(i, n):
        product = (product * arr[i]) / (count)
        if product > previous:
            previous = count
        s += f"{previous} "
        count += 1
    print(s)

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print_permute(n, arr)
main()