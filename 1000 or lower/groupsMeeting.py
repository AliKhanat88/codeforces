
def printPossible(arr, n):
    combination = []
    counts = []
    for i in range(5):
        count = 0
        for j in range(n):
            count += arr[j][i]
        if count >= n //2:
            combination.append(i)
            counts.append(count)
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            count = 0
            for k in range(n):
                count += (arr[k][combination[i]] & arr[k][combination[j]])
            remaining1 = counts[i] - (count)
            remaining2 = counts[j] - (count)
            if remaining1 >= remaining2:
                temp = remaining1 + count - (n//2)
                if temp + remaining2 >= n // 2:
                    print("YES")
                    return
            else:
                temp = remaining2 + count - (n//2)
                if temp + remaining1 >= n // 2:
                    print("YES")
                    return
    print("NO")     



def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [0] * n
        for j in range(n):
            arr[j] = [int(num) for num in input().split()]
        printPossible(arr, n)

main()