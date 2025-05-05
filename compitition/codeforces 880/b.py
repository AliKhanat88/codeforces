from math import ceil
for t in range(int(input())):
    n, k, g = map(int, input().split())
    half = ceil(g / 2)
    sumi = (half - 1) * (n-1)
    if sumi >= g * k:
        print(g*k)
        continue
    if g - sumi % g >= half:
        sumi -= sumi % g
    else:
        sumi += (g - sumi % g)
    print(sumi)
