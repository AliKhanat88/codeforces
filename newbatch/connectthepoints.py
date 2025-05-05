def solve():
    x1, y1 = map(int, input().split())

    x2, y2 = map(int, input().split())

    x3, y3 = map(int, input().split())

    arr = [(x1, y1), (x2, y2), (x3, y3)]
    
    arr.sort(key=lambda x: x[1])
    x1, y1 = arr[0][0], arr[0][1]
    x2, y2 = arr[1][0], arr[1][1]
    x3, y3 = arr[2][0], arr[2][1]
    ans = []

    ans.append((x1, y1, x1, y2))
    ans.append((x1, y2, x2, y2))

    if x3 >= min(x1, x2) and x3 <= max(x1, x2):
        ans.append((x3, y3, x3, y2))
    else:
        ans.append((x3, y3, x3, y2))
        if abs(x3 - x1) <= abs(x3 - x2):
            ans.append((x3, y2, x1, y2))
        else:
            ans.append((x3, y2, x2, y2))
    print(len(ans))
    for seg in ans:
        print(seg[0], seg[1], seg[2], seg[3])



solve()