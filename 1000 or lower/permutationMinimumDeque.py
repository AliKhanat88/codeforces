from collections import deque

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dq = deque()
        dq.append(arr[0])
        for i in range(1, n):
            if arr[i] < dq[0]:
                dq.appendleft(arr[i])
            else:
                dq.append(arr[i])
        for i in range(n):
            print(dq[i], end=" ")
        print()

main()


        
