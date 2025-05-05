
def check_velly(arr):
    r = len(arr)
    if r == 1:
        print("YES")
        return
    count = 0
    if arr[1] > arr[0]:
        count += 1
    for i in range(1, r-1):
        if arr[i] < arr[i-1] and arr[i+1] > arr[i]:
            if count > 0:
                print("NO")
                return
            count += 1
    if arr[r-2] > arr[r-1]:
        count += 1
    if count == 1:
        print("YES")
    else:
        print("NO")
        
    

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        if n == 1:
            print("YES")
            continue
        real_arr = [int(arr[0])]
        for num in arr:
            if int(num) != real_arr[-1]:
                real_arr.append(int(num))
        check_velly(real_arr)

main()