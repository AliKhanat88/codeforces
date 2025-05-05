def solve():
    # print("test")
    n, m ,h = map(int, input().split())
    temp_arr = list(map(int, input().split()))
    r_p = 0
    r_pen = 0
    temp_arr.sort()
    time = 0
    i = 0
    while i < m and time + temp_arr[i] <= h:
        r_p += 1
        r_pen = r_pen + time + temp_arr[i]
        time += temp_arr[i]
        i += 1
    # print(r_p)
    pos = 1
    for i in range(n-1):
        temp_arr = list(map(int, input().split()))
        temp_p = 0
        temp_arr.sort()
        time = 0
        pen = 0
        i = 0
        while i < m and time + temp_arr[i] <= h:
            temp_p += 1
            pen = pen + time + temp_arr[i]
            time += temp_arr[i]
            i += 1
        # print(temp_p)
        if temp_p > r_p or (temp_p == r_p and pen < r_pen):
            pos += 1
    print(pos)

 

for t in range(int(input())):
    solve()

