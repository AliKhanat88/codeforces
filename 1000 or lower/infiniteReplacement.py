def checkReplacement(string, replacer):
    temp_a = set(string)
    temp_b = set(replacer)
    if len(replacer) > 1:
        for char in temp_a:
            if char in temp_b:
                print(-1)
                return
    permute = 1
    for charac in string:
        if charac != replacer:
            permute *= 2

    print(permute)




def main():
    t = int(input())
    for i in range(t):
        string = input()
        replacer = input()
        checkReplacement(string, replacer)


main()