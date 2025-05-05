def solve():
    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    complete = set()
    adj = [[] for i in range(n+1)]
    for i in range(n):
        if arr1[i] == arr2[i]:
            complete.add((arr1[i], i))
        adj[arr1[i]].append(i)
        adj[arr2[i]].append(i)
    
    print(adj)
    ans = 1
    MOD = 998244353
    visited = set()
    visited_index = set()
    for num in complete:
        if num not in visited:
            stack = [num]
            ans = (ans * n) % MOD
            while stack:
                print(stack)
                cur = stack.pop()
                if cur[0] in visited:
                    print(0)
                    return
                visited.add(cur[0])
                visited_index.add(cur[1])
                for child in adj[cur[0]]:
                    if child == cur[1]:
                        pass
                    else:
                        if child in visited_index:
                            print(0)
                            return
                        elif arr1[child] not in visited:
                            stack.append((arr1[child], child))
                        else:
                            stack.append((arr2[child], child))
    
    for i in range(n):
        if arr1[i] in visited and arr2[i] in visited:
            continue
        elif arr1[i] not in visited and arr2[i] not in visited:
            stack = [(arr1[i], i)]
            can1 = True
            new_visited1 = set()
            new_visited1_index = set()
            while stack:
                print(stack)
                cur = stack.pop()
                if cur[0] in new_visited1:
                    can1 = False
                    break
                new_visited1.add(cur[0])
                for child in adj[cur[0]]:
                    if child == cur[1]:
                        pass
                    else:
                        if child == i:
                            continue
                        elif arr1[child] in new_visited1 and arr2[child] in new_visited1:
                            print(0)
                            return
                        elif arr1[child] not in new_visited1:
                            stack.append((arr1[child], child))
                        else:
                            stack.append((arr2[child], child))

            #second
            stack = [(arr2[i], i)]
            can2 = True
            new_visited2 = set()
            while stack:
                print(stack)
                cur = stack.pop()
                if cur[0] in new_visited2:
                    can2 = False
                    break
                new_visited2.add(cur[0])
                for child in adj[cur[0]]:
                    if child == cur[1]:
                        pass
                    else:
                        if child == i:
                            continue
                        elif arr1[child] in new_visited2 and arr2[child] in new_visited2:
                            print(0)
                            return
                        elif arr1[child] not in new_visited2:
                            stack.append((arr1[child], child))
                        else:
                            stack.append((arr2[child], child))
            if can1 == False and can2 == False:
                print(0)
                return
            elif can1 == True and can2 == True:
                ans = (ans * 2) % MOD
            if can1 == True:
                for num in new_visited1:
                    visited.add(num)
            else:
                for num in new_visited2:
                    visited.add(num)
        else:
            raise Exception()

    print(ans)



                

        
for t in range(int(input())):
    solve()