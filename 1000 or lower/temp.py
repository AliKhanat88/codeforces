def check_max_diff(length, list):
    diff = 0
    for i in range(length):
        if list[i] - list[0] > diff:
            diff = list[i] - list[0]
        if list[-1] - list[i] > diff:
            diff = list[-1] - list[i]
        if list[i-1] - list[i] > diff:
            diff = list[i-1] - list[i]
    print(diff)
from pickle import *

def main():
    a = [i for i in range(10**9)]
    for i in range(2, 10**9 // 2):
        for j in range(i+i, 10**9, i):
            a[j] = -1
    f = open("abc.bin", "wb")
    dump(a, f)
    f.close()
    
main()