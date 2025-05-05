def main():
    x = int(input())
    dict = {True:"YES", False:"NO"}

    print(dict[x % 2 == 0 and x > 2])





main()