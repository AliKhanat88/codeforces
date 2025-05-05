def print_count(n,m,arr):
    s = ""
    set_arr = set()
    i = 0
    length = 0
    count = 0
    while i < m and count < n:
        set_arr.add(arr[i])
        if len(set_arr) != length:
            s = f" {i+1}" + s
            count += 1
            length += 1
        i = i + 1
    if n - length > 0:
        s = (n-length) * " -1" + s
    print(s[1:])

def main():
    t=int(input())
    for j in range(t):
        n, m= map(int,input().split())
        set_arr = list(map(int, input().split()))
        print_count(n,m,set_arr)
main()