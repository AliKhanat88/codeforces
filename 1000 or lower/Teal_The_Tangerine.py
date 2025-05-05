def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        count = 0
        list = input()
        first = ""
        for j in range(len(list)):
            if list[j] == " ":
                break
            first += list[j]
        list = list.split()
        if int(first) == 1:
            for j in range(n):
                count += int(list[j]) - 1
        else:
            double = int(first) * 2
            for j in range(n):
                count += int((int(list[j])) / (double - .9999999))
        print(count)

main()