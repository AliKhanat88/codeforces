def main():
    n = int(input())
    a = int(input())
    b = int(input())
    if n == 1:
        if a == b:
            print(1)
            print(f"{a}:{b}")
        else:
            print(0)
            print(f"{a}:{b}")
        return
    if n > a + b:
        draws = n - a - b
    else:
        draws = 0
    print(draws)
    temp = n-draws-3
    while temp >= 0 and a > 1:
        print("1:0")
        temp -= 1
        a -= 1
    while temp >= 0 and b > 1:
        print("0:1")
        temp -= 1
        b -= 1
    
    if a == 0 and b != 0:
        print(f"0:1")
        print(f"0:{b-1}")
    elif b == 0 and a != 0:
        print(f"1:0")
        print(f"{a-1}:0")
    elif a != 0 and b != 0:
        print(f"{a}:0")
        print(f"0:{b}")
    for i in range(draws):
        print("0:0")


main()