from collections import defaultdict
import sys
input = sys.stdin.readline
from itertools import permutations
from random import randint


def solve(n, songs):
    graph1 = defaultdict(lambda: [])
    graph2 = defaultdict(lambda: [])
    # arr = []
    for i in range(n):
        a, b = songs[i]
        graph1[i].append(a)
        graph1[i].append(b)
        graph2[a].append((i, 0))
        graph2[b].append((i, 1))

    # print(graph1)
    # print(graph2)
    # print(arr)

    def dfs(node):
        maxi = 1
        stack = [(node, -1)]
        path = [-1]
        visited = set()
        visited.add(-1)
        while len(stack) != 0:
            cur = stack.pop()
            # break
            while cur[1] != path[-1]:
                visited.remove(path.pop())
            if cur[0] not in visited:
                # print(cur)
                # print(path, node)
                path.append(cur[0])
                visited.add(cur[0])
                maxi = max(maxi, len(path) - 1)
                for child in graph2[graph1[cur[0]][0]]:
                    if child[1] == 0:
                        stack.append((child[0], cur[0]))
                for child in graph2[graph1[cur[0]][1]]:
                    if child[1] == 1:
                        stack.append((child[0], cur[0]))
            
            
            
        return maxi
            
    maxi = 0
    for i in range(n):
        maxi = max(maxi, dfs(i))
    print(n - maxi)
    return n - maxi

    
def main():
    for t in range(int(input())):
        n = int(input())
        songs = []
        for i in range(n):
            songs.append(input().strip().split())
        solve(n, songs)


main()

def brute(n, songs):
    perms = list(permutations(songs, n))
    maxi = 0
    for i in range(len(perms)):
        count = 1
        for j in range(1, n):
            if perms[i][j][0] == perms[i][j-1][0] or perms[i][j][1] == perms[i][j-1][1]:
                count += 1
            else:
                break
        maxi = max(maxi, count)
    return n - maxi

# print(brute(3, [("a", "b"), ("a", "b"), ("b", "a")]))

def checker():
    n = 5
    for i in range(100000):
        songs = []
        for i in range(n):
            songs.append((f"{randint(1, 5)}", f"{randint(1, 5)}"))
        if brute(n, songs) != solve(n, songs):
            print("Found")
            print(songs)
            print(brute(n, songs))
            print(solve(n, songs))
            break

# checker()

# solve(5, [('5', '3'), ('1', '2'), ('3', '5'), ('5', '5'), ('5', '2')])
