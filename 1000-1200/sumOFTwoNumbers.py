def print_combin(n):
    num = n
    num1 = ""
    num2 = ""
    is_first = True
    while num > 0:
        digit = num % 10
        if digit % 2 == 1:
            if is_first == True:
                num1 = f"{digit // 2 + 1}"+num1
                is_first = False
                num2 = f"{digit // 2}" + num2
            else:
                num2 = f"{digit // 2 + 1}"+num2
                is_first = True
                num1 = f"{digit // 2}"+num1
        else:
            num1 = f"{digit // 2}"+num1
            num2 = f"{digit // 2}" + num2
        num = num // 10
    print(int(num1), int(num2))

def main():
    for i in range(int(input())):
        n = int(input())
        print_combin(n)
main()