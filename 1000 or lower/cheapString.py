def print_string(n, p , arr):
    result = 0
    is_greater = False
    result_arr = [""] * n
    for i in range(ord("a"), ord("z") + 1):
        for j in range(n):
            if arr[j] == chr(i): 
                result += i - 96
                if result > p:
                    is_greater = True
                    break
                result_arr[j] = chr(i)
        if is_greater == True:
            break  
    print("".join(result_arr))
def main():
    t = int(input())
    for i in range(t):
        arr = list(input())
        p = int(input())
        n = len(arr)
        print_string(n, p , arr)


main()