from collections import defaultdict

def print_sorting_group(books, groups, list, count_list):
    for i in range(groups):
        for j in range(books // groups):
            is_zero = False
            if count_list[chr(97 + j)] - i<= 0:
                print(chr(97 + j), end = "") 
                is_zero = True
                break
        if is_zero == False:
            print(chr(97 + books // groups), end="")
    

def main():
    t = int(input())
    for i in range(t):
        books, groups = map(int, input().split())
        list = input()
        count_list = defaultdict(int)
        for i in range(books):
            count_list[list[i]] += 1
        print_sorting_group(books, groups, list, count_list)
        print()

main()