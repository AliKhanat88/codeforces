import sys
input = sys.stdin.readline

def print_longest(n, a, a_bar):
    i = 0
    last = 0
    points = [0, 0]
    while i < n-1:
        if a_bar[i] > a_bar[i+1]:
            j = last
            poss = False
            while j < i:
                if a[j] > a[j+1]:
                    poss = True
                    break
                j += 1
            if poss == True:
                if points[1] - points[0] < i - last:
                    points = [last+1, i+1]
            last = i + 1
        i += 1
    i = n -1
    while i > 0 :
        if a_bar[i-1] > a_bar[i]:
            j = n-1
            poss = False
            while j > i:
                if a[j-1] > a[j]:
                    poss = True
                    break
                j -= 1
            if poss == True:
                if points[1] - points[0] < n-1 - i:
                    points = [i + 1, n-1 +1]
            break
        i -= 1
    if  i == 0:
        print(1, n)
    else:
        print(points[0], points[1])
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_bar = list(map(int, input().split()))
    print_longest(n, a, a_bar)