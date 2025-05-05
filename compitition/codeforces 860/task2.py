from collections import defaultdict
def print_poss(m):
    days = [0] * m
    data = []
    dict = defaultdict(lambda:0)
    for i in range(m):
        n = int(input())
        arr = list(map(int, input().split()))
        for j in range(n):
            dict[arr[j]] += 1
        data += arr
        days[i] = n
    print(dict)
    print(data)
    # per = -1
    # r = ""
    # for i in range(m):
    #     isone = False
    #     j = per + 1
    #     while j < days[i] + per + 1:
    #         if check_data[j] != -1:
    #             r += f"{data[j]} "
    #             isone = True
    #             break
    #         j += 1
    #     if isone == False:
    #         print(-1)
    #         return
    #     per += days[i]
    # print(r)
        
def main():
    for t in range(int(input())):
        m = int(input())
        print_poss(m)

main()