def solve():
    n = int(input())
    sets = [[i+1] for i in range(n)]
    for i in range(n):
        s = input()
        for j in range(n):
            if s[j] == "1":
                sets[j].append(i+1)
    for set in sets:
        print(len(set), end= " ")
        print(" ".join([str(num) for num in set]))

for t in range(int(input())):
    solve()