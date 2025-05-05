from math import ceil

def check_doable(n, k):
    if ceil((n * k) / 2) % k != 0:
        print("NO")
        return
    print("YES")
    j = 1
    for i in range(1, n * k + 1, 2):
        print(i, end=" ")
        j += 1
        if j > k:
            print()

    j = 1
    for i in range(2, n * k + 1, 2):
        print(i, end=" ")
        j += 1
        if j > k:
            print()
    



def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        check_doable(n, k)

main()