from collections import defaultdict
def print_permutation(n, data):
    count_dict = defaultdict(lambda:0)
    for j in range(n):
        count_dict[data[j][0]] += 1
    temp = list(count_dict.items())
    if temp[0][1] > temp[1][1]:
        first_value = temp[0][0]
    else:
        first_value = temp[1][0]
    r = f"{first_value} "
    for i in range(n-1):
        for j in range(n):
            if data[j][i] != first_value:
                r += f"{data[j][i]} "
                first_value = data[j][i]
                break
    print(r)

def main():
    for i in range(int(input())):
        n = int(input())
        data = [0] * n
        for j in range(n):
            arr = list(map(int, input().split()))
            data[j] = arr
        print_permutation(n, data)

main()