def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = [[], [], []]
    for i in range(n-1, -1, -1):
        count[arr[i]].append(i)
    ans = []
    one = count[1][-1]
    if len(count[0]) >= len(count[2]):
        zeros = sorted(count[0][:])
        # print(one, "one")
        for i in range(len(count[0])):
            if arr[i] == 1:
                arr[i], arr[zeros[-1]] = arr[zeros[-1]], arr[i]
                ans.append((i, zeros[-1]))
                one = zeros[-1]
                zeros.pop()
            elif arr[i] == 2:
                ans.append((i, one))
                ans.append((i, zeros[-1]))
                arr[i] = 0
                arr[one] = 2
                arr[zeros[-1]] = 1
                one = zeros[-1]
                zeros.pop()
            # print(arr, one)
        count = [[], [], []]
        for i in range(n):
            count[arr[i]].append(i)
        
        for i in range(len(count[0]), len(count[0]) + len(count[1])):
            if arr[i] == 2:
                ans.append((i, count[1][-1]))
                count[1].pop()
    else:
        # print("hey")
        twos = sorted(count[2][:], reverse=True)
        # print(one, "one")
        for i in range(len(count[2])):
            index = n - i - 1
            if arr[index] == 1:
                arr[index], arr[twos[-1]] = arr[twos[-1]], arr[index]
                ans.append((index, twos[-1]))
                one = twos[-1]
                twos.pop()
            elif arr[index] == 0:
                ans.append((index, one))
                ans.append((twos[-1], index))
                arr[index] = 2
                arr[one] = 0
                arr[twos[-1]] = 1
                one = twos[-1]
                twos.pop()
            # print(arr, one)
        count = [[], [], []]
        for i in range(n):
            count[arr[i]].append(i)
        
        for i in range(len(count[0])):
            if arr[i] == 1:
                ans.append((i, count[0][-1]))
                count[0].pop() 

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0] + 1, ans[i][1] + 1)
    # print(ans)

                



    

for t in range(int(input())):
    solve()