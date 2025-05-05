def print_s(n, index_s):
    index_s = sorted(index_s, key = lambda x : x[1])
    r = ""
    for i in range(n):
        if index_s[i][0] < i:
            temp = index_s[i][1] - index_s[i][0] + i
            if temp < 8:
                r += f"{temp}"
            else:
                r += "9"
        else:
            r += f"{index_s[i][1]}"

    print(r)
def main():
    for i in range(int(input())):
        s= input()
        n = len(s)
        index_s = [(i, int(s[i])) for i in range(n)]
        print_s(n, index_s)

main()