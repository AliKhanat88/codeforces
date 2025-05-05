def solve(n):
    ans1 = -1
    ans2 = -1
    for i in range(0, n, 2):

        if n % 2 == 1 and i == n-1:
            print(f"! {i+1}", flush=True)
            return
        if n % 2 == 0 and i == n - 2:
            ans1 = i+1
            ans2 = i+2
            break
        a = i
        b = (i+1) % n
        print(f"? {a+1} {b+1}", flush=True)
        temp1 = input()
        if temp1 == "-1":
            quit()
        print(f"? {b + 1} {a + 1}", flush=True)
        temp2 = input()
        if temp2 == "-1":
            quit()
        if temp1 != temp2:
            ans1 = a + 1
            ans2 = b + 1
            break
    for i in range(1, n+1):
        if i != ans1 and i != ans2:
            ans3 = i
            break
    # print(ans1, ans2, ans3)
    print(f"? {ans1} {ans3}", flush=True)
    temp1 = input()
    if temp1 == "-1":
        quit()
    print(f"? {ans3} {ans1}", flush=True)
    temp2 = input()
    if temp2 == "-1":
        quit()
    if temp1 != temp2:
        print(f"! {ans1}", flush=True)
        return
    
    print(f"! {ans2}", flush=True)
    
    



for t in range(int(input())):
    n = int(input())
    solve(n)