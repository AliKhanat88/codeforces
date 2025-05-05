def main():
    n = int(input())
    for i in range(n):
        nums = int(input())
        if nums % 2 == 0:
            print(nums // 2)
        else:
            print(nums // 2 + 1)
            print(nums // 2 * 3 + 1 , nums // 2 * 3 + 3)
        temp = nums // 2 
        for j in range(temp):
                print(j * 3 + 1, (nums - j)* 3)


main()




