def query(type, arg1=None, arg2=None):
    if type == "+":
        print(f"{type} {arg1}", flush=True)
    else:
        print(f"{type} {arg1} {arg2}", flush=True)
    output = int(input())
    if output == -2:
        exit()
    return output

def solve():
    n = int(input())
    query("+", n+1)
    query("+", n)
    
    edges = []
    for i in range(n):
        # print(i+1, n-i)
        if i + 1 > n - i:
            break
        if i + 1 == n - i:
            edges.append(i + 1)
            continue
        edges.append(n - i)
        edges.append(i+1)
    edges= edges[::-1]
    # print(edges)
    maxi = -1
    maxi_node = None
    for i in range(2, n+1):
        temp = query("?", 1, i)
        if temp > maxi:
            maxi = temp
            maxi_node = i
    assert maxi_node != None
    
    ans1 = [0] * (n+1)
    ans2 = [0] * (n+1)
    ans1[maxi_node] = edges[0]
    ans2[maxi_node] = edges[-1]

    for  i in range(1, n+1):
        if i != maxi_node:
            temp_ans = query("?",maxi_node, i)
            # print(temp_ans, n - temp_ans)
            ans1[i] = edges[temp_ans]
            ans2[i] = edges[n - temp_ans -1]


    print("!", *ans1[1:], *ans2[1:])
    temp = int(input())
    if temp == -2:
        exit()
    

for t in range(int(input())):
    solve()