for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    sumi = sum(arr)
    sumi = sumi - maxi
    if sumi + maxi == 0:
        print(0)
    elif maxi - sumi <= 1:
        print(1)
    else:
        print(maxi - sumi)