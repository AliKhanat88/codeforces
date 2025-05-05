from random import randint
from collections import defaultdict

def solve():
    randi = randint(1, 2 ** 64)
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    seti = defaultdict(lambda: 0)
    def query(num):
        temp = num ^ randi
        return seti[temp] >= 1
    def add(num):
        temp = num ^ randi
        seti[temp] += 1
    def rem(num):
        temp = num ^ randi
        seti[temp] -= 1
    
    for num in a:
        add(num)
    count = len(a)
    stack = b
    while True:
        if len(stack) <= 0:
            if count == 0:
                print("YES")
                return
            else:
                print("NO")
                return
        cur = stack.pop()
        if cur == 1 and query(cur) == False:
            print("NO")
            return
        if query(cur) == True:
            rem(cur)
            count -= 1
            continue
        if cur % 2 == 0:
            stack.append(cur // 2)
            stack.append(cur // 2)
        else:
            stack.append(cur // 2)
            stack.append(cur // 2 + 1)
        # print(stack)
        
        

for t in range(int(input())):
    solve()