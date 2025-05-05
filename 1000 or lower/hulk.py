def main():
    n = int(input())
    dict1 = {1:"I hate that ", 0:"I love that "}
    dict2 = {1:"I hate it ", 0:"I love it "}
    for i in range(1, n):
        print(dict1[i % 2], end="")
    print(dict2[n%2])



main()
