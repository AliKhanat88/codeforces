from collections import defaultdict

def solve():
    n = int(input())
    arr = list(input())
    dict = defaultdict(lambda:-1)

    rem = [chr(num) for num in range(ord("a"), ord("z")+1)]

    for i, char in enumerate(arr):
        if dict[char] == -1:
            if len(rem) == 1:
                dict[char] = rem.pop(-1)
            else:
                for num in rem:
                    temp = num
                    done = True
                    while temp != -1:
                        if temp == char:
                            done = False
                            break
                        temp = dict[temp]
                    if done == True:
                        dict[char] = num
                        rem.remove(num)
                        break
        print(dict[char], end="")
    print()

    # print(rem)
    # print(length)

for t in range(int(input())):
    solve()