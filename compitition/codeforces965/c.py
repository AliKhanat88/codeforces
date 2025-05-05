from heapq import heappop, heappush

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = [(arr[i], brr[i]) for i in range(n)]
    crr.sort()
    # print("TEST")
    # print(arr)
    # print(brr)
    # print(crr, k)

    max0 = -1
    max1 = -1
    for i in range(n):
        if crr[i][1] == 1:
            max1 = max(max1, crr[i][0])
        else:
            max0 = max(max0, crr[i][0])
    # print(max0)
    # print(max1)
    maxi = -1
    if max1 != -1:
        index = -1
        for i in range(n):
            if crr[i][0] == max1:
                index = i
        if index + 1 > n // 2:
            maxi = max1 + crr[n // 2 - 1][0] + k
        else:
            maxi = max1 + crr[n // 2][0] + k
        # print(maxi)
    if max0 != -1 and crr[-1][0] == max0:
        crr.pop()
        left = n // 2 - 1
        total = []
        equal = None
        count = 0
        while left >= 0:
            if crr[left][1] == 1:
                equal = crr[left][0]
                count = 1
                left -= 1
                break
            else:
                total.append(crr[left][0])
            left -= 1
        right = n // 2
        if equal != None:
            while k >= 0:
                if right >= len(crr):
                    break
                if count * (crr[right][0] - equal) <= k:
                    k -= count * (crr[right][0] - equal)
                    equal = crr[right][0]
                else:
                    break
                if crr[right][1] == 0:
                    total.append(crr[right][0])
                    right += 1
                    found = False
                    while left >= 0:
                        if crr[left][1] == 1:
                            if equal - crr[left][0] <= k:
                                count += 1
                                k -= (equal - crr[left][0])
                            else:
                                total.append(crr[left][0] + k)
                                k = 0
                            left -= 1
                            found = True
                            break
                        else:
                            total.append(crr[left][0])
                        left -= 1
                    if found == False:
                        break
                else:
                    right += 1
                    count += 1
        # print("here", left, right, left)
        if count > 0:
            temp = count
            for i in range(k % count):
                total.append(equal + k // count + 1)
                temp -= 1
            for i in range(temp):
                total.append(k // count + equal)

        for i in range(right, len(crr), 1):
            total.append(crr[i][0])
        for i in range(left, -1, -1):
            total.append(crr[i][0])
        # print(total)
        total.sort()
        if len(total) < len(crr):
            print(total)
            raise Exception()
        maxi = max(maxi, total[n // 2 - 1] + max0)
    print(maxi)

                
for t in range(int(input())):
    solve()