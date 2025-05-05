from collections import defaultdict
def minimum_dolls(n, arr):
    arr.sort()
    dict = defaultdict(lambda : 0)
    for i in range(n):
        dict[arr[i]] += 1
    count = 0
    temp = list(dict.keys())
    for i in range(len(temp)):
        if dict[temp[i]] - dict[temp[i]-1]> 0:
            count += (dict[temp[i]] - dict[temp[i]-1])
    print(count)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        minimum_dolls(n, arr)

main()