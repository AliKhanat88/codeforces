from collections import defaultdict
def print_possible(n, s):
    dict = defaultdict(lambda:-1)
    start = 0
    is_ok = True
    for i in range(n):
        if dict[s[i]] == -1:
            dict[s[i]] = start
        elif dict[s[i]] != start and dict[s[i]] != -1:
            is_ok = False
            break
        if start == 0:
            start = 1
        else:
            start = 0
    if is_ok == True:
        print("YES")
        return
    dict = defaultdict(lambda:-1)
    start = 1
    for i in range(n):
        if dict[s[i]] == -1:
            dict[s[i]] = start
        elif dict[s[i]] != start and dict[s[i]] != -1:
            print("NO")
            return
        if start == 0:
            start = 1
        else:
            start = 0
    print("YES")

def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        print_possible(n, s)

main()