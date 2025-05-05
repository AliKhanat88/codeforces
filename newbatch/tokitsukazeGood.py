def solve(n, s):

    arr_black = []
    count = 0
    per = s[0]
    for i in range(n):
        if s[i] == per:
            count += 1
        else:
            arr_black.append(count)
            count = 1
            per = s[i]

    arr_black.append(count)
    # print(arr_black)
    if s[0] == "0":
        isWhite = True
    else:
        isWhite = False
    arr_white = arr_black[:]
    ans_white = 0
    ans_black = 0
    oper = 0
    for i in range(len(arr_black)-1):
        if arr_black[i] % 2 != 0 and arr_white[i] % 2 != 0:
            oper += 1
            if isWhite:
                arr_white[i+1] -= 1
                arr_black[i+1] += 1
                arr_black[i] -= 1
                arr_white[i] += 1
                if arr_black[i] == 0:
                    if i-1 >= 0:
                        arr_black[i+1] = arr_black[i+1] + arr_black[i-1]
                    chance1 = max(0, ans_black - 1)
                else:
                    chance1 = ans_black + 1
                ans_white = ans_white + 1
                ans_black = chance1
            else:
                arr_black[i+1] -= 1
                arr_white[i+1] += 1
                arr_black[i] += 1
                arr_white[i] -= 1
                if arr_white[i] == 0:
                    if i-1 >= 0:
                        arr_white[i+1] = arr_white[i+1] + arr_white[i-1]
                    chance1 = max(0, ans_white - 1)
                else:
                    chance1 = ans_white + 1
                ans_black = ans_black + 1
                ans_white = chance1
        elif arr_black[i] % 2 != 0 or arr_white[i] % 2 != 0:
            print(s)
            raise Exception("")
        else:
            if arr_black[i] != 0:
                ans_black += 1
            else:
                arr_black[i+1] = arr_black[i-1] + arr_black[i+1]
                ans_black = max(0, ans_black - 1)
            if arr_white[i] != 0:
                ans_white += 1
            else:
                arr_white[i+1] = arr_white[i-1] + arr_white[i+1]
                ans_white = max(0, ans_white - 1)
        if arr_black[i+1] > 1 and arr_white[i+1] > 1:
            if ans_black > ans_white:
                ans_black = ans_white
                arr_black[i+1] = arr_white[i+1]
            elif ans_white > ans_black:
                ans_white = ans_black
                arr_white[i+1] = arr_black[i+1]



        isWhite = not isWhite
    
    if arr_white[-1] != 0:
        ans_white += 1
    if arr_black[-1] != 0:
        ans_black += 1
    print(oper, min(ans_black, ans_white))
    return min(ans_black, ans_white)

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        s = input()
        solve(n, s)