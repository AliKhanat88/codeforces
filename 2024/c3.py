from collections import defaultdict

def solve():
    n = int(input())
    stack = [1]
    tree = defaultdict(lambda:[])
    for i in range(2, n+1):
        tree[1].append(i)

    # print(tree)
    arr_ans = []
    while len(arr_ans) < n-1:
        new_tree = defaultdict(lambda:[])
        new_stack = []
        for cur in range(1, n+1):
            for child in tree[cur]:
                print(f"? {cur} {child}")
                ans = int(input())
                if ans == -1:
                    raise Exception()
                if ans == cur:
                    arr_ans.append(f"{cur} {child}")
                    new_stack.append(child)
                else:
                    new_tree[ans].append(child)
        tree = new_tree
        stack = new_stack
        # print(tree)
        # print(stack)
    print("!" ," ".join(arr_ans))

        


for t in range(int(input())):
    solve()