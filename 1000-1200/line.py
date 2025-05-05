def print_changes(n, s):
    arr = [0] * n
    perfect = [0] * n
    for i in range(n):
        if s[i] == "L":
            arr[i] = i
        else:
            arr[i] = n - i - 1
    for i in range(n-1, n//2-1, -1):
        perfect[i] = i
    for i in range(n//2):
        perfect[i] = n-i-1
    is_first = True
    org = sum(arr)
    first = 0
    last = n-1
    temp = 0
    for i in range(1, n+1):
        while first <= last:
            if is_first == True:
                is_first = False
                if arr[first] != perfect[first]:
                    temp = first
                    first += 1
                    break
                first += 1
            elif is_first == False:
                is_first = True
                if arr[last] != perfect[last]:
                    temp = last
                    last -= 1
                    break
                last -= 1
        
        org -= arr[temp]
        org += perfect[temp]
        arr[temp] = perfect[temp]
        print(org, end= " ")
    print()

def main():
    for t in range(int(input())):
        n = int(input())
        s = input()
        print_changes(n, s)

main()