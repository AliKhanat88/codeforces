import sys
input = sys.stdin.readline

def print_poss(m):
    days = [0] * m
    data = []
    check_data = []
    for i in range(m):
        n = int(input())
        arr = list(map(int, input().split()))
        for j in range(n):
            for index, value in enumerate(data):
                if value == arr[j]:
                    check_data[index] = -1
        data += arr
        days[i] = n
        check_data += [0] * n
    per = -1
    r = ""
    for i in range(m):
        isone = False
        j = per + 1
        while j < days[i] + per + 1:
            if check_data[j] != -1:
                r += f"{data[j]} "
                isone = True
                break
            j += 1
        if isone == False:
            print(-1)
            return
        per += days[i]
    print(r)
        
def main():
    for t in range(int(input())):
        m = int(input())
        print_poss(m)

main()