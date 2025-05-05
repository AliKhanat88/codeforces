def print_max_sum(n, m, arr_n, arr_m):
    # print(arr_m, arr_n)
    for i in range(m):
        arr_n.sort()
        arr_n[0] = arr_m[i]
        # print(arr_n, i)

    print(sum(arr_n))

def main():
    for i in range(int(input())):
        n, m = map(int, input().split())
        arr_n = list(map(int, input().split()))
        arr_m = list(map(int, input().split()))
        print_max_sum(n, m, arr_n, arr_m)
main()