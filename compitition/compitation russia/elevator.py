def main():
    d = int(input())
    if d > 0:
        clicks = d // 3
        remaining = d % 3
        if remaining == 1:
            clicks += 2
        elif remaining == 2:
            clicks += 4
    elif d < 0:
        clicks = d // -2
        remaining = d % 2
        if remaining == 1:
            clicks += 3
    else:
        clicks = 0
    print(clicks)

main()
