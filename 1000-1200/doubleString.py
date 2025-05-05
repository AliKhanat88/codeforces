from collections import defaultdict
def print_str(n, data):
    dict = defaultdict(lambda:0)
    for i in range(n):
        dict[data[i]] = 1
    # print(dict)
    c = ""
    for i in range(n):
        if len(data[i]) > 1:
            is_done = False
            # print(data[i])
            for j in range(1, len(data[i])):
                # print(data[i][:j], data[i][j:])
                if dict[data[i][:j]] == 1 and dict[data[i][j:]] == 1:
                    c += "1"
                    is_done = True
                    break
            if is_done == False:
                c += "0"
        else:
            c += "0"
    print(c)
            

for t in range(int(input())):
    n = int(input())
    data = [""] * n
    for i in range(n):
        data[i] = input()
    print_str(n, data)
