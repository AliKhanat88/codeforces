import sys
input = sys.stdin.readline

def print_poss(n, arr_a, arr_b):
    for i in range(n-1):
        if (arr_b[i] > arr_b[i+1] + 1 and arr_a[i] != arr_b[i]) or arr_a[i] > arr_b[i]:
            print("NO")
            return
    if (arr_b[-1] > arr_b[0] + 1 and arr_a[-1] != arr_b[-1]) or arr_a[-1] > arr_b[-1]:
        print("NO")
        return
    print("YES")


for t in range(int(input())):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    print_poss(n, arr_a, arr_b)
