def print_latest(data):
    for i in range(8):
        is_same = True
        for j in range(8):
            if data[i][j] != "R":
                is_same = False
                break
        if is_same == True:
            print("R")
            return
    print("B")    




def main():
    n = int(input())
    for i in range(n):
        input()
        data = []
        for j in range(8):
            data.append(input().rstrip())
        print_latest(data)



main()