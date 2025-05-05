def solve():
    n, s1, s2 = map(int, input().split())
    arr = input().split()
    arr = [(i+1, int(arr[i])) for i in range(n)]
    arr.sort(key=lambda x:x[1], reverse=True)

    temp1 = s1
    temp2 = s2
    output1 = []
    output2 = []
    for i in range(n):
        if temp1 <= temp2:
            output1.append(str(arr[i][0]))
            temp1 += s1
        else:
            output2.append(str(arr[i][0]))
            temp2 += s2
    print(len(output1), " ".join(output1))
    print(len(output2), " ".join(output2))
    


for t in range(int(input())):
    solve()