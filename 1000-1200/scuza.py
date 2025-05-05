def print_max_steps(n, q, steps, ques):
    pair_list = [0] * q
    for i, value in enumerate(ques):
        pair_list[i] = (i, value)
    ques = sorted(pair_list, key=lambda x: x[1])
    previous = 0
    j = 0
    s = [0] * q
    i = 0
    while i < q:
        if j < n and ques[i][1] >= steps[j]:
            previous += steps[j]
            j = j + 1
        else:
            s[ques[i][0]] = f"{previous}"
            i = i + 1
    print(" ".join(s))
def main():
    t= int(input())
    for i in range(t):
        n, q = map(int, input().split())
        steps = list(map(int, input().split()))
        ques = list(map(int, input().split()))
        print_max_steps(n, q, steps, ques)

main()
