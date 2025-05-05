def main():
    t = int(input())
    for i in range(t):
        w, h = map(int, input().split())
        horizontal_0 = list(map(int, input().split()))
        horizontal_h = list(map(int, input().split()))
        vertical_0 = list(map(int, input().split()))
        vertical_w = list(map(int, input().split()))
        result1 = abs(horizontal_0[1] - horizontal_0[-1]) * h
        result2 = abs(horizontal_h[1] - horizontal_h[-1]) * h
        result3 = abs(vertical_0[1] - vertical_0[-1]) * w
        result4 = abs(vertical_w[1] - vertical_w[-1]) * w
        print(max(result1, result2, result3, result4))

main()
