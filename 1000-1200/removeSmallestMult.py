def print_min_cost(n, arr):
    cost = 0
    i = 1
    mark = [1] * n
    while i <= n:
        if arr[i-1] != "1":
            j = i
            while j <= n and arr[j-1] != "1":
                if mark[j-1] != "0":
                    cost += i
                    mark[j-1] = "0"
                j += i
        i = i + 1
    print(cost)
def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(input())
        print_min_cost(n, arr)
 
main()