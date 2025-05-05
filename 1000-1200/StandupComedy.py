def main():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        matches = a
        maxi = max(b,c)
        mini = min(b,c)
        if a + b + c + d == 0:
            print(0)
            continue
        if a > 0:
            matches += mini * 2
            maxi = maxi - mini
        if d - a > 0:
            matches += a
            print(matches + 1)
            continue
        else:
            matches += d
            a -= d
            if maxi - a > 0:
                matches += a + 1
            elif maxi - a == 0:
                matches += a
            else:
                matches += maxi
            print(matches) 

main()