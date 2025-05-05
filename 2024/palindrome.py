for t in range(int(input())):
    n = int(input())
    arr = ["a", "e", "i", "o", 'u']
    if n <= 5:
        print("".join(arr[:n]))
    else:
        print("".join(arr[:5]) + "u" * (n - 5))