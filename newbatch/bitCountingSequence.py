def solve(n, arr):
    if n == 1:
        if arr[0] == 0:
            print(0)
        else:
            print(int("".join(["1"] * arr[0]), 2))
        return
    if n == 2:
        if arr[0] == 0:
            if arr[1] == 1:
                print(0)
            else:
                print(-1)
        elif arr[1] == 0 or arr[1] > arr[0] + 1:
            print(-1)
        elif arr[0] == arr[1] - 1:
            print(int("".join(["1"] * (arr[1])), 2) - 1)
        
        elif arr[0] == arr[1]:
            print(int("".join(["1"] * (arr[1]+1)), 2) - 2)
        elif arr[0] > arr[1]:
            if arr[1] == 1:
                print(int("".join(["1"] * arr[0]), 2))
            else:
                temp = ["1"] * (arr[0] + 1)
                temp[arr[1] - 1] = "0"
                print(int("".join(temp), 2))
        return

    predict = []
    if arr[0] == 0:
        for i in range(n):
            predict.append(i)
    elif arr[1] == 0 or arr[1] > arr[0] + 1:
        print(-1)
        return
    elif arr[0] == arr[1] - 1:
        if arr[1] == arr[2]:
            temp = int("".join(["1"] * (arr[2] + 1)), 2)

            predict = [temp-3, temp-2, temp-1, temp]
        elif arr[2] > arr[1] or arr[2] == 0:
            print(-1)
            return
        else:
            temp = int("".join(["1"] * (arr[1])), 2)
            predict = [temp-1, temp]
    elif arr[0] == arr[1]:
        temp = int("".join(["1"] * (arr[1] + 1)), 2)
        predict = [temp - 2, temp - 1, temp]
    elif arr[0] > arr[1]:
        temp = int("".join(["1"] * arr[0]), 2)
        predict = [temp]
    # print(predict)
    if 0 in arr[1:]:
        print(-1)
        return
    predict = predict[::-1]
    ans = [0] * n
    for i in range(n):
        if len(predict) == 0:
            if arr[i] >= arr[i - 1]:
                print(-1)
                return
            if arr[i] == 1:
                start = ["0"] * arr[i-1]
                start.insert(0, "1")
                start = int("".join(start), 2) + 1
                ans[i] = start - 1

                j = i + 1
                while j < n:
                    predict.append(start)
                    start += 1
                    j += 1
            else:
                start = ["0"] * (arr[i-1] + 1)
                for j in range(arr[i]):
                    start[j] = "1"
                start = int("".join(start), 2) + 1
                ans[i] = start - 1
                j = i + 1
                while j < n and bin(start).count("1") < arr[i-1] + 1:
                    predict.append(start)
                    start += 1
                    j += 1
                predict.append(start)
            predict = predict[::-1]
        else:
            if bin(predict[-1]).count("1") != arr[i]:
                print(-1)
                return
            ans[i] = predict.pop()
    # print(ans)
    print(ans[-1] - n + 1)

if __name__ =="__main__":
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n ,arr)