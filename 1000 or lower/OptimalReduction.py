from collections import defaultdict

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        k = 1
        while k < n and arr[k] >= arr[k-1]:
            k = k +1
        j = k
        while j < n and arr[j] <= arr[j -1]:
                j += 1
        if j == n:
            print("YES")
        else:
            print("No")



main()