for t in range(int(input())):
    s = input()
    count_question = 0
    for i in range(1, len(s)):
        if s[i] == "?":
            count_question += 1
    if s[0] == "0":
        print(0)
    elif count_question == 0 and s[0] != "?":
        print(1)
    elif s[0] == "?" and count_question == 0:
        print(9)
    elif s[0] == "?":
        print(10 ** count_question * 9)
    else:
        print(10 ** count_question)