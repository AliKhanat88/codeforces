def check_str(n, k, s):
    mini = k
    count = 0
    first = 0
    i = 0
    while i < k:
        if s[i] == "W":
            count += 1
        i += 1
            
    if count < mini:
        mini = count
    for i in range(k, n):
        if s[first] == "W":
            count -= 1
        if s[i] == "W":
            count += 1
        first += 1
        if count < mini:
            mini = count
        
    print(mini)
def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        s = input()
        check_str(n, k, s)

main()