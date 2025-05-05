def get_pair(data, length):
    if length % 2 != 0:
        print(-1)
        return
    else:
        count = 0
        arr = []
        raw = ""
        for i in range(0, length, 2):
            if data[i] == data[i+1]:
                count += 1
                raw = raw + f"\n{i+1} {i+2}"
            else:
                count += 2
                raw = raw + f"\n{i+1} {i+1}\n{i+2} {i+2}"
    print(count, end="")
    print(raw)



def main():
    n = int(input())
    for i in range(n):
        length = int(input())
        data = list(map(int, input().split()))
        get_pair(data, length)
        
main()