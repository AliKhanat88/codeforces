def is_palindrome_seq(n, arr):
    arr = sorted(arr, key = lambda x: len(x))
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i+1][::-1]:
            print("NO")
            return
        i = i + 2
    print("YES")
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        is_palindrome_seq(n, arr)

main()