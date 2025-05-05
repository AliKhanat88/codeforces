def solve():
    s = input()
    dict = [[(0,) for i in range(len(s)+1)] for i in range(len(s)+1)]

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            dict[i-1][i] = (True, min(s[i], s[i-1]), max(s[i], s[i-1]))
        else:
            dict[i-1][i] = (False, s[i], s[i-1])
    for d in range(2, len(s)):
        for i in range(d, len(s)):
            if d % 2 == 0:
                if dict[i-d][i-1][0] == False and dict[i-d+1][i][0] == False:
                    if s[i-d] < s[i]:
                        dict[i-d][i] = (False, dict[i-d+1][i][1], s[i-d])
                    else:
                        dict[i-d][i] = (False, dict[i-d][i-1][1], s[i])
                elif dict[i-d][i-1][0] == False:
                    dict[i-d][i] = (False, dict[i-d][i-1][1], s[i])
                elif dict[i-d+1][i][0] == False:
                    dict[i-d][i] = (False, dict[i-d+1][i][1], s[i-d])
                else:
                    dict[i-d][i] = (True, dict[i-d+1][i][1], s[i-d])    
                pass  
            elif d % 2 == 1:
                if dict[i-d][i-1][0] == False and dict[i-d+1][i][0] == False:
                    if s[i-d] < dict[i-d+1][i][2]:
                        dict[i-d][i] = (True, s[i-d], dict[i-d+1][i][2])
                    elif s[i] < dict[i-d][i-1][2]:
                        dict[i-d][i] = (True, s[i], dict[i-d][i-1][2])
                    else:
                        dict[i-d][i] = (False, s[i], dict[i-d][i-1][2])
                elif dict[i-d][i-1][0] == True:
                    dict[i-d][i] = (True, s[i], dict[i-d][i-1][2])
                else:
                    dict[i-d][i] = (True, s[i-d], dict[i-d+1][i][2])
                pass
    if dict[0][len(s)-1][0] == False:
        print("Draw")
        return "Draw"
    else:
        print("Alice")
        return "Alice"
if __name__ == "__main__":
    for t in range(int(input())):
        solve()