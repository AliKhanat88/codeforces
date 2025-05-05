def print_min_zero(n, arr):
    i = n-1
    while i > 0:
        if arr[i] < arr[i-1]:
            break
        i -= 1
    if i == 0:
        print(0)
        return
    check_set = set(arr[:i])
    inter_set = check_set & set(arr[i:])
    j = n-1
    while j >= i:
        if arr[j] in inter_set:
            print(len(set(arr[:j+1])))
            return
        j -= 1
    print(len(check_set))
    
def main():
    for i in range(int(input())):
        n = int(input())
        arr = input().split()
        print_min_zero(n, arr)
 
main()