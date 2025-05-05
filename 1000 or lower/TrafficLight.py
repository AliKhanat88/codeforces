def main():
    n = int(input())
    for k in range(n):
        length, ch = input().rstrip().split()
        length = int(length)
        seq = input().rstrip()
        counts = []
        i = 0
        if ch == "g":
            print(0)
        else:
            while i < length:
                if seq[i] == ch:
                    j = i
                    count = 0
                    while j < length:
                        if j == length - 1 and seq[j] != "g":
                            j = -1
                            i = length
                        elif seq[j] == "g":
                            counts.append(count)
                            break
                        j = j + 1
                        count += 1
                    i = i + count
                i=i+1
            print(max(counts))
                


main()