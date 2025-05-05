def checkWinning(n, s):
    count = 0
    for i in range(n):
        if s[i] != "1":
            count += 1
    if count > 2 or count < 1:
        print("YES")
        goal = 2
        for i in range(n):
            k = 0
            for j in range(n):
                if s[j] == "2":
                    if i != j:
                        k = k + 1 
                    if j == i:
                        print("X", end="")
                    elif i == 0 and j == n-1:
                        print("-", end="")
                    elif i == n-1 and j == 0:
                        print("+", end="")
                    elif k == goal:
                        print("+", end="")
                    elif k == goal - 1:
                        print("-", end="")
                else:
                    print("=", end="")
            goal = goal + 1
            print()
    else:
        print("NO")
    


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        checkWinning(n, s)

main()