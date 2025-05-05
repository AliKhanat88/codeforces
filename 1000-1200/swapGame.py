def main():
    for i in range(int(input())):
        n = int(input())
        arr = input().split()
        arr[0] = int(arr[0])
        mini = 999999999
        for i in range(1, n):
            arr[i] = int(arr[i])
            if arr[i] < mini:
                mini = arr[i]
        if arr[0] > mini:
            print("Alice")
        else:
            print("Bob")
main()