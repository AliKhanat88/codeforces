def print_possible(n, prr):
    prr.sort()
    sum = 1
    if prr[0] != 1:
        print("NO")
        return
    for i in range(1, n):
        if prr[i] > sum:
            print("NO")
            return
        sum += prr[i]
    print("YES")

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print_possible(n, arr)

main()