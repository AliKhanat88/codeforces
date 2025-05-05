
        
# print(valid(3, [1, 3, 2], [2, 1, 3]))
def main():
    for i in range(1, 1500):
        n = compute_oper(i)
        print(n)
        ans = solve(n)
        seti = set()
        for i in range(1, len(ans)):
            if ans[i] * ans[i-1] in seti:
                print("FOund", i)
                return
            seti.add(ans[i] * ans[i-1])

        # if sorted(ans) != sorted(ans2):
        #     print(n, count)
        #     break
main()