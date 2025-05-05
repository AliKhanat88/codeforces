def maximum_reach(left, right, mini, initial, end):
    if initial == end:
        print(0)
        return
    if abs(left - initial) < mini and abs(right-initial) < mini:
        print(-1)
        return
    if abs(end-initial) >= mini:
        print(1)
        return
    if (abs(initial - left) >= mini and abs(left-end) >= mini) or (abs(initial-right) >= mini and abs(right-end) >= mini):
            print(2)
            return
    if (abs(initial - left) >= mini and abs(left-end) < mini and abs(right - end) >= mini) or (abs(initial-right) >= mini and abs(right-end) < mini and abs(left - end) >= mini):
            print(3)
            return
    print(-1)

def main():
    for i in range(int(input())):
        left, right, mini = map(int, input().split())
        initial, end = map(int, input().split())
        maximum_reach(left, right, mini, initial, end)
main()