def print_mat(n):
    data = [[0 for i in range(n)] for i in range(n)]
    guesser = 2
    num = 1
    second_guess = 2
    for i in range(n):
        if guesser % 2 == 0:
            for j in range(n):
                if second_guess % 2 == 0:
                    data[i][j] = str(num)
                else:
                    data[i][j] = str(n * n - num + 1)
                    num += 1
                second_guess += 1
                
        else:
            for j in range(n-1, -1, -1):
                if second_guess % 2 == 0:
                    data[i][j] = str(num)
                else:
                    data[i][j] = str(n * n-num+1)
                    num += 1
                second_guess += 1
        guesser += 1
    for i in range(n):
        print(" ".join(data[i]))

def main():
    for i in range(int(input())):
        n = int(input())
        print_mat(n)

main()