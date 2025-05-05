def main():
    for t in range(int(input())):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        i = 0
        mini = 9999999999
        while i < n:
            # print(i, arr[i], end = " ")
            count = 1
            temp = arr[i]
            while True:
                if temp % x == 0:
                    # print(temp, end = " ")
                    count += 1
                    temp = temp // x
                else:
                    break
            if count < mini:
                mini = count
                index = i
            # print(count)
            i += 1
        sumi = 0
        for i in range(index):
            sumi += arr[i] * (mini + 1)
        for j in range(index, n):
            sumi += arr[j] * (mini)
        print(sumi)
main()