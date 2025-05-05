default = -99999999999999999999999
def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    sumi = 0
    stack = []
    for i in range(n):
        sumi += arr[i]
        if sumi <= 0:
            sumi = 0
            continue
        if arr[i] <= 0:
            continue
        while len(stack) != 0 and arr[i] >= stack[-1][0]:
            if sumi - stack[-1][1] + stack[-1][0] > arr[i]:
                print("NO")
                return
            stack.pop()
        if len(stack) >= 1:
             if sumi - stack[-1][1] + stack[-1][0] > stack[-1][0]:
                print("NO")
                return

        stack.append((arr[i], sumi))
    print("YES")

for t in range(int(input())):
    solve()