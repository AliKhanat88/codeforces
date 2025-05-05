def print_spells(n, arr):
    arr.sort()
    i = 0
    goal = 1
    speels = 0
    while i < n:
        if arr[i] == goal:
            j = i + 1
            while j < n and arr[j] == goal:
                j += 1
            i = j - 1
            goal += 1
        elif arr[i] != goal:
            speels += (arr[i] - goal)
            goal += 1
        i = i + 1
    print(speels)

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print_spells(n, arr)

main()