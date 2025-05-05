def print_max_jump(n, arr):
    i = 1
    max = 0
    while i <= n:
        jump = i
        is_jump = True
        while jump <= n:
            # print(jump, end=" ")
            if arr[jump-1] == -1:
                is_jump = False
                break
            temp = arr[jump-1]
            arr[jump-1] = -1
            jump = jump + temp
        if is_jump == True and jump - i > max:
            max = jump - i
        # print(jump- i)
        i += 1
    print(max)



def main():
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print_max_jump(n, arr)

main()