def check_max_diff(length, list):
    diff = 0
    for i in range(length):
        if list[i] - list[0] > diff:
            diff = list[i] - list[0]
        if list[-1] - list[i] > diff:
            diff = list[-1] - list[i]
        if list[i-1] - list[i] > diff:
            diff = list[i-1] - list[i]
    print(diff)
def main():
    t= int(input())
    for i in range(t):
        length = int(input())
        list = [int(num) for num in input().split()]
        check_max_diff(length, list)
    
main()