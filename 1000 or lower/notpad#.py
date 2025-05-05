from collections import defaultdict

def check_less_operations(n, string):
    two_comb = defaultdict(lambda: 0)
    for i in range(1, n):
        two_comb[string[i-1:i+1]] += 1
        if two_comb[string[i-1:i+1]] >= 2:
            if string[i-2:i] == string[i-1:i+1] and two_comb[string[i-1:i+1]] == 2:
                continue
            print("YES")
            return
    print("NO")
        

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        string = input()
        check_less_operations(n, string)


main()