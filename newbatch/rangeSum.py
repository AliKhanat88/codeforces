def solve():
    i = int(input())
    if i == 2:
        print(3, 1)
    elif i == 3:
        print(3, 6, 7)
    elif i == 4:
        print(25, 21, 23, 31)
    else:
        lower = i - i
        higher = i
        while lower + 1 < higher:
            mid = lower + (higher - lower) // 2
            temp = ((mid + mid + (i+1)) * (i + 2)) // 2
            if temp - (i + 1) ** 2 >= mid + 2 + mid + 1 and temp - (i + 1) ** 2 <= mid + i + i - 1:
                lower = mid
                higher = mid
                break
            elif temp - (i + 1) ** 2 < mid + 2 + mid + 1:
                lower = mid + 1
            elif temp - (i + 1) ** 2 > (mid + i + i - 1):
                higher = mid - 1

        temp = ((lower + lower + (i+1)) * (i + 2)) // 2
        if temp - (i + 1) ** 2 >= lower + 2 + lower + 1 and temp - (i + 1) ** 2 <= lower + i + i - 1:
            arr = [j for j in range(lower, lower + i + 2)]
            if (temp - (i + 1) ** 2) % 2 == 0:
                arr.remove((temp - (i + 1) ** 2) // 2 - 1)
                arr.remove((temp - (i + 1) ** 2) // 2 + 1)
            else:
                arr.remove((temp - (i + 1) ** 2) // 2)
                arr.remove((temp - (i + 1) ** 2) // 2 + 1)
            print(*arr)
            return
        temp = ((higher + higher + (i+1)) * (i + 2)) // 2
        if temp - (i + 1) ** 2 >= higher + 2 + higher + 1 and temp - (i + 1) ** 2 <= higher + i + i - 1:
            # print("YES")
            arr = [j for j in range(higher, higher + i + 2)]
            if (temp - (i + 1) ** 2) % 2 == 0:
                # print("YES")
                arr.remove((temp - (i + 1) ** 2) // 2 - 1)
                arr.remove((temp - (i + 1) ** 2) // 2 + 1)
            else:
                arr.remove((temp - (i + 1) ** 2) // 2)
                arr.remove((temp - (i + 1) ** 2) // 2 + 1)
            print(*arr)
            return
    
if __name__ == "__main__":
    for t in range(int(input())):
        solve()