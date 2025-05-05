def main():
    t = int(input())
    for i in range(t):
        r, c = map(int, input().split())
        temp = c // 3
        count = r * temp
        c = c - (temp* 3)
        if c <= 0:
            print(count)
            continue
        temp = r // 3
        r = r - (temp * 3)
        count += (temp * c)
        if r == 1 and c == 1:
            count += 1
        count += (r*c // 2)
        print(count)

main()