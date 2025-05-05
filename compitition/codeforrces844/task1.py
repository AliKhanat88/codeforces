def main():
    t = int(input())
    for i in range(t):
        w, d, h = map(int, input().split())
        a, b, f, g = map(int, input().split())
        if b + g > (d-b + d-g):
            temp_b = d-b
            temp_g = d-g
        else:
            temp_b = b
            temp_g = g
        result1 = h + abs(a - f) + temp_b + temp_g
        if a + f > (w-a+w-f):
            a = w-a
            f = w-f
        result2 = h + abs(b-g) + a + f
        if result1 < result2:
            print(result1)
        else:
            print(result2)

main()