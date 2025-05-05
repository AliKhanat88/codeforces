def solve():
    a = input()
    arr = []
    cur_int = ""
    cur_word = ""
    count_open = 0
    i = 0
    while i < len(a):
        if a[i] == "[":
            count_open += 1
            while i < len(a) and ord(a[i]) >= ord("a") and ord(a[i]) <= ord("z"):
                cur_word += a[i]
                i += 1
            arr.append([count_open, int(cur_int), cur_word])
            cur_int = ""
            cur_word = ""
        elif a[i] == "]":
            count_open -= 1
        elif ord(a[i]) >= ord("0") and ord(a[i]) <= ord("9"):
            cur_int += a[i]
        i += 1
    print(arr)





for t in range(int(input())):
    solve()