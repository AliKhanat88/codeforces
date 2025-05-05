
def solve():
    n, m = map(int, input().split())
    stack = [(1, n)]
    for i in range(m):
        a, b = map(int, input().split())
        mini = min(a, b)
        maxi = max(a,b)
        ind = 0
        while ind < len(stack):
            if stack[ind][0] <= mini and stack[ind][1] >= maxi:
                temp = stack[ind]
                if temp[0] - maxi-1 == 0:
                    stack.pop(ind)
                else:
                    stack[ind] = (temp[0], maxi-1)
                if mini+1 - temp[1] != 0:
                    stack.append((mini+1,temp[1]))
            ind += 1
    check_set = set()
    sumi = 0
    mini = 99999999999999999
    maxi = 0
    print(sumi)
for t in range(int(input())):
    solve()
    
