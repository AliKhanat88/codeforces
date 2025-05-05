def print_paths(n, parents): 
    temp_set = set(parents)
    temp_set.add(n+1)
    temp_set = list(temp_set)
    temp_set.sort()

    paths = []
    per = 1
    for i in range(len(temp_set)):
        while per != temp_set[i] and per <= n:
            num = per
            path = []
            while parents[num-1] != -1:
                path.append(num)
                temp = parents[num-1]
                parents[num-1] = -1
                num = temp
            paths.append(path)
            per += 1
        per += 1
    print(len(paths))
    for path in paths:
        print(len(path))
        print(" ".join(str(x) for x in reversed(path)))

for t in range(int(input())):
    n = int(input())
    parents = list(map(int, input().split()))
    if n == 1:
        print(1)
        print(1)
        print(1)
    else:
        print_paths(n, parents)
    