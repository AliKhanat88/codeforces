
def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        arr = list(map(int,input().split()))
        pos = 0
        arr.sort()
        count = 0
        while pos < n-1:
            temp = arr.pop(-1)
            count += 1
            pos += n - temp
            k -= 1
            if k <= 0 or pos >= arr[-1]:
                break
        print(count)
        
main()