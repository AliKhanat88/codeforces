def main():
    n = int(input())
    for i in range(n):
        length = int(input())
        s = input()
        count = 0
        for i in range(length):
            if s[i] == "Q":
                count += 1
            elif s[i] == "A" and count > 0:
                count -= 1
        if count > 0:
            print("No")
        else:
            print("Yes")


main()