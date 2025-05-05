def print_pos(n, arr1, arr2):
    maxi1 = max(arr1[:-1])
    maxi2 = max(arr2[:-1])
    if maxi1 > arr1[-1] and maxi2 > arr2[-1]:
        print("NO")
        return
    elif maxi1 <= arr1[-1] and maxi2 <= arr2[-1]:
        print("YES")
        return
    elif maxi1 <= arr1[-1]:
        for i in range(n):
            if arr2[i] > arr1[-1] and arr2[i] > arr2[-1]:
                print("NO")
                return
            if arr1[i] > arr2[-1] and arr2[i] > arr2[-1]:
                print("NO")
                return
    elif maxi2 <= arr2[-1]:
        for i in range(n):
            if arr1[i] > arr1[-1] and arr1[i] > arr2[-1]:
                print("NO")
                return
            if arr1[i] <= arr2[-1]:
                if arr1[i] > arr1[-1] and arr2[i] > arr1[-1]:
                    print("NO")
                    return
    print("YES")
            

def main():
    for t in range(int(input())):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        if n == 1:
            print("YES")
        else:
            print_pos(n, arr1, arr2)

main()