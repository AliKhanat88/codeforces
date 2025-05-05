def get_pair(data, length):
    nonzero_length = 0
    for i in range(length):
        if data[i] != 0:
            nonzero_length += 1
    if nonzero_length % 2 != 0:
        print(-1)
        return
    else:
        count = 0
        i = 0
        raw = ""
        while i < length:
            if data[i] == 0:
                raw = raw + f"\n{i+1} {i+1}"
                count += 1
                i = i + 1
            elif data[i] == data[i+1]:
                count += 1
                raw = raw + f"\n{i+1} {i+2}"
                i = i + 2   
            elif data[i+1] == 0:
                temp = i
                i += 1
                while i < length and data[i] == 0:
                    i  = i + 1
                
                if data[temp] == data[i] and i - temp % 2 == 0:
                        print()
                    raw = raw + f"\n{temp+1} {i+1}"
                    i = i + 1
                    count += 1
                elif temp != data[i]:
                    raw = raw + f"\n{i+1} {i+1}\n{i+2} {i+2}"
                    count += 2
                    i = i + 1
            else:
                count += 2
                raw = raw + f"\n{i+1} {i+1}\n{i+2} {i+2}"
                i = i + 2
    print(count, end="")
    print(raw)



def main():
    n = int(input())
    for i in range(n):
        length = int(input())
        data = list(map(int, input().split()))
        get_pair(data, length)
        
main()