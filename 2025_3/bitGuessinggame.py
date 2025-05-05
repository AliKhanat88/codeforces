def solve():
    bits = int(input())

    def query(x):
        print(f"- {x}", flush=True)
        temp = int(input())
        if temp == -1:
            exit()
        return temp
    
    c = 0
    ans = 0
    for i in range(bits):
        temp = query(1 << c)
        c += (temp - (bits - 1))
        bits = temp
        ans += (1 << c)
    print(f"! {ans}",flush=True)

for t in range(int(input())):
    solve()