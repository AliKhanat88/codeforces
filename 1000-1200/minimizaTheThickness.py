def print_min(n, arr):
    maximums = [n]
    for i in range(n):
        maxi = i+1
        per = i
        for j in range(i+1, n):
            if arr[j] - arr[per] == arr[i]:
                if maxi < (j - per):
                    maxi = j - per
                per = j
        if per == n-1:
            maximums.append(maxi)
    print(min(maximums))
                    
def main():
    for i in range(int(input())):
        n = int(input())
        arr = input().split()
        arr[0] = int(arr[0])
        for i in range(1, n):
            arr[i] = arr[i-1] + int(arr[i])
        print_min(n, arr)

main()