from collections import defaultdict
def print_queries(n, k, arr):
    dorg = sum(arr)
    dict = defaultdict(lambda:-1)
    for i in range(k):
        a, b, q = map(int, input().split())
        if dict[(a,b)] != -1:
            temp_sum = dict[(a,b)]
        else:
            temp_sum = sum(arr[a-1:b])
            dict[(a,b)] = temp_sum
        if (dorg - temp_sum + ((b - a + 1) * q)) % 2 == 1:
            print("YES")
        else:
            print("NO")
def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print_queries(n, k, arr)

main()