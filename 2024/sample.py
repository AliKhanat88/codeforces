l = 1
r = 10 ** 6

while l + 1 < r:
    m = (l + r) // 2
    print(m, flush=True)
    ans = input()
    if ans == ">=":
        l = m
    else:
        r = m - 1
print(r, flush=True)
ans = input()
if ans == ">=":
    print(f"! {r}")
else:
    print(f"! {l}")