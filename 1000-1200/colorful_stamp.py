def print_is_pos(n, s):
    arr = s.split("W")
    for val in arr:
        if len(val) == 1:
            print("NO")
            return
        elif val != "":
            if all_same(val) == True:
                print("No")
                return
    print("YES")
def all_same(s):
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            return False
    return True

def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        print_is_pos(n, s)
main()