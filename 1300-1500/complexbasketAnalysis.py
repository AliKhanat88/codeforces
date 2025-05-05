prime = [0] * (10**6 + 1)
prime[1] = -1
for i in range(3, 500001, 2):
    for j in range(i+i+i, 1000001, 2 * i):
        prime[j] = -1

def is_prime(num):
    if (num % 2 == 1 and prime[num] == 0) or num == 2:
        return True
    return False

def solve():
    n, e = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    sumi = 0
    for i in range(e):
        j = i
        count = 0
        per_count = 0
        per = False
        while j < n:
            if arr[j] == 1:
                count += 1
                if per == True:
                    sumi += per_count
            elif is_prime(arr[j]):
                sumi += count
                per = True
                per_count = count + 1
                count = 0
            else:
                count = 0
                per = False
            j += e
        # print(sumi)
    print(sumi)



for t in range(int(input())):
    solve()


