def check_difference(a, b):
    sumi = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            sumi += 1
    return sumi

def sol(t):
    # print("test", t+1)
    n = int(input())
    first = input()
    second = input()
    reversed_second = second[::-1]
    good_count = check_difference(first, second)
    ungood_count = check_difference(first, reversed_second)
    if good_count % 2 == 1:
        good_count = good_count + good_count - 1
    elif good_count % 2 == 0:
        good_count = good_count + good_count
    if ungood_count == 0:
        ungood_count = 2
    elif ungood_count % 2 == 1:
        ungood_count = ungood_count + ungood_count
    elif ungood_count % 2 == 0:
        ungood_count = ungood_count + ungood_count -1
    print(min(good_count, ungood_count))


for t in range(int(input())):
    sol(t)