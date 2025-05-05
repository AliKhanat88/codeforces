def check_matches(numOfPlayers, x, y):
    if x == 0 and y == 0:
        print(-1, end="")
        return
    if x == 0:
        temp = y
    elif y == 0:
        temp = x
    else:
        print(-1, end="")
        return
    if (numOfPlayers - 1) % temp == 0:
        for i in range(2, numOfPlayers+1, temp):
            print(f"{i} " * temp, end="")
    else:
        print(-1, end="")

def main():
    n = int(input())
    for i in range(n):
        numOfPlayers, x, y = map(int, input().split())
        check_matches(numOfPlayers, x, y)
        print()

main()