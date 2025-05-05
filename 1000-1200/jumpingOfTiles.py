
def print_cost_index(s):
    n = len(s)
    first = s[0]
    last = s[-1]
    r = f"1 "
    cost = 0
    count = 2
    if first == last:
        for i in range(1, n-1):
            if s[i] == first:
                r += f"{i+1} "
                count += 1
        r += f"{n} "
        print(cost, count)
        print(r)
        return
    index_chr = [0] * (n-2)
    for i in range(1, n-1):
        index_chr[i-1] = (s[i], i+1)
    if ord(first) < ord(last):
        index_chr = sorted(index_chr, key=lambda x: ord(x[0]))
        i = 0
        while i < n-2:
            if ord(index_chr[i][0]) >= ord(first):
                break
            i = i + 1
        for i in range(i, n-2):
            if ord(index_chr[i][0]) > ord(last):
                break
            r += f"{index_chr[i][1]} "
            count += 1
        cost = abs(ord(last) - ord(first))
        r += f"{n} "
        print(cost, count)
        print(r)
    elif ord(first) > ord(last):
        index_chr = sorted(index_chr, key=lambda x: ord(x[0]), reverse=True)
        i = 0
        while i < n-2:
            if ord(index_chr[i][0]) <= ord(first):
                break
            i = i + 1
        for i in range(i, n-2):
            if ord(index_chr[i][0]) < ord(last):
                break
            r += f"{index_chr[i][1]} "
            count += 1
        cost = abs(ord(last) - ord(first))
        r += f"{n} "
        print(cost, count)
        print(r)
    

def main():
    for i in range(int(input())):
        s = input()
        print_cost_index(s)

main()