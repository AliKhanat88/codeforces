def print_max_days(n, must_have):
    must_have = sorted(must_have, key=lambda x: x[0] - x[1])
    days = 0
    first = 0
    for i in range(n-1, -1, -1):
        if first >= i:
            break
        if must_have[first][0] + must_have[i][0] <= must_have[first][1] + must_have[i][1]:
            days += 1
            first += 1
    print(days)

def main():
    for i in range(int(input())):
        n = int(input())
        must = input().split()
        have = input().split()
        must_have = [(int(must[i]), int(have[i])) for i in range(n)]
        print_max_days(n, must_have)

main()