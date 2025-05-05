def main():
    for t in range(int(input())):
        n , T = map(int, input().split())
        arr = list(map(int, input().split()))
        s = set()
        for i in range(n):
            # print(arr[i], s)
            if arr[i] > T:
                print("1", end = " ")
                # pass
            else:
                if T - arr[i] in s:
                    print("0", end=" ")
                    # pass
                else:
                    print("1", end= " ") 
                    # pass
                s.add(arr[i])
        print()

main()