def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        para = 0
        maximum = 0
        for j in range(n):
            temp1, temp2 = input().split(" ")
            temp1 = int(temp1)
            temp2 = int(temp2)
            if temp1 < temp2:
                maxi = temp2
                mini = temp1
            else:
                maxi = temp1
                mini = temp2
            if maximum < maxi:
                maximum = maxi
            para += mini * 2
        para += maximum * 2
        print(para)
main() 