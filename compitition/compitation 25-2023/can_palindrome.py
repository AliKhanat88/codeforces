def check_palindrome(n,s):
    for i in range(n // 2):
        if s[i] != s[n-1-i]:
            break
    is_equal = True
    is_not_equal = True
    for i in range(i, n // 2):
        if s[i] != s[n-i-1]:
            is_equal = False
        else:
            is_not_equal = False
        if is_equal == False and is_not_equal == False:
            break
    for i in range(i+1, n // 2):
        if s[i] != s[n-i-1]:
            print("NO")
            return
    print("YES")  




def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        check_palindrome(n,s)


main()