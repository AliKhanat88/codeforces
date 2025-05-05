from math import log2

def makeGood(n, arr):
    op = 0
    r = ""
    for i in range(n):
        temp = log2(arr[i])
        if temp % 1 !=  0:
            op += 1
            r += f"{i+1} {2 ** (int(temp)+1) - arr[i]}\n"
    print(op)
    if r != "":
        print(r[:-1])

           

def main():
    for i in range(int(input())):
        n = int(input())
        arr= list(map(int, input().split()))
        makeGood(n, arr)

main()