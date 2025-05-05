def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    index_arr = [(b[i], i)  for i in range(n)]
    index_arr.sort(key=lambda x:x[0])
    # print("TEST")
    # print(a)
    # print(b)
    # print(index_arr)
    for i, num in enumerate(index_arr):
        if a[num[1]] != num[0]:
            done = False
            start = num[1]
            while start > -1:
                if b[start] < num[0]:
                    break
                elif a[start] > num[0]:
                    break
                elif a[start] == num[0]:
                    done = True
                    break
                start -= 1
            if done == True:
                for j in range(start, num[1]+1):
                    a[j] = num[0]
            else:
                start = num[1]
                while start < n:
                    if b[start] < num[0]:
                        break
                    elif a[start] > num[0]:
                        break
                    elif a[start] == num[0]:
                        done = True
                        break
                    start += 1
            if done == True:
                for j in range(num[1], start+1):
                    a[j] = num[0]
            else:
                print("NO")
                return
            # print(f"num[0]: {num[0]}")
            # print(a)
            # print(b)
    # print(a)
    # print(b)
    for i in range(n):
        if a[i] != b[i]:
            print("NO")
            return
    print("YES")
for t in range(int(input())):
    solve()