def solve():
    sumi = int(input())
    for char in range(ord("a"), ord("z")+1):
        for char1 in range(ord("a"), ord("z")+1):
            for char2 in range(ord("a"), ord("z")+1):
                if char + char1 + char2 - ((ord("a") - 1) * 3) == sumi:
                    print(chr(char) + chr(char1) + chr(char2))
                    return
for t in range(int(input())):
    solve()