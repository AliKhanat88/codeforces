# from math import pow
import random
# n = 1
# i = 3
# sum = 3
# while sum < 10 ** 9:
#     i += 2
#     sum += i
#     n += 1
# print(n)
n = 20000
# arr = ["3 1 0\n2 2 2" for i in range(n)]
# file = open("input.txt", "w")
# file.write(f"{n}\n")
# file.write("\n".join(arr))
# file.close()


# # topological sort
#     top_sort_tree = [0] * (n+1)
#     index = 1
#     visited = [False] * (n+1)
#     queue = [(top, -1, 0)]

#     while len(queue) != 0:    
#         new_queue = []
#         for i in range(len(queue)):
#             for child in graph[queue[i][0]]:
#                 visited[queue[i][0]] = True
#                 if not visited[child]:
#                     new_queue.append((child, index, queue[i][2]+1))
#             top_sort_tree[index] = (queue[i][1], queue[i][2])
#             index += 1
#         queue = new_queue


# import sys
# all_input = sys.stdin.readlines()

# print(all_input)

# temp = set()
# temp.add(1)
# temp.add(2)
# temp.add(3)
# print(temp.remove(3))

# Trie
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, num):
        cur = self.root
        for b in range(20, -1, -1):
            if num & (2 ** b) != 0:
                temp = 1
            else:
                temp = 0
            done = False
            for n in cur.children:
                if n.val == temp:
                    cur = n
                    done = True
            if done:
                continue
            temp = Node(temp)
            cur.children.append(temp)
            cur = temp
    def get_max(self, num):
        ans = 0
        cur = self.root
        for b in range(20, -1, -1):
            temp = (num & (2 **b)) // (2**b)
            if len(cur.children) == 0:
                return ans
            elif len(cur.children) == 1:
                if cur.children[0].val != temp:
                    ans += (2 ** b)
                cur = cur.children[0]
            else:
                for child in cur.children:
                    if child.val != temp:
                        ans += (2 ** b)
                        cur = child
        return ans

def print_tree(root):
    stack = [(root , 0)]
    while len(stack) != 0:
        cur = stack.pop()
        print(cur[1] * " ", cur[0].val)
        for child in cur[0].children:
            stack.append((child, cur[1] + 1))




t = Trie()
t.insert(9)
t.insert(4)


print_tree(t.root)

print(t.get_max(16))