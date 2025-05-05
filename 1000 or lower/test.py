def check_velly(arr):
    r = len(arr)
    if r == 1:
        print("NO")
        return
    count = 0
    for i in range(1, r-1):
        if (arr[i] < arr[i-1] or arr[i-1] == 0) and (arr[i+1] > arr[i] or arr[i+1] == 0):
            if count > 0:
                print("NO")
                return
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
        real_arr = [0]
        for num in arr:
            if int(num) != real_arr[-1]:
                real_arr.append(int(num))
        real_arr.append(0)
        check_velly(real_arr)

main()