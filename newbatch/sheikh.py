def solve():
    n, _ = map(int, input().split())

    arr = list(map(int, input().split()))

    bit_count_ideal = [0] * 31
    for i in range(n):
        for b in range(31):
            if arr[i] & (2 ** b) != 0:
                bit_count_ideal[b] += 1
    input()

    bit_count = [0] * 31
    i = 0
    done = False
    while i < n:
        new_count = bit_count[:]
        for b in range(31):
            if arr[i] & (2 ** b) != 0:
                if bit_count_ideal[b] % 2 == 1:
                    if new_count[b] + 1 >= 2:
                        done = True
                        break
                    else:
                        new_count[b] += 1
                else:
                    if new_count[b] + 1 >= 1:
                        done = True
                        break
                    else:
                        new_count[b] += 1
        if done:
            break
        bit_count = new_count
        i += 1
    done = False
    j = n-1
    while j >= i:
        new_count = bit_count[:]
        for b in range(31):
            if arr[j] & (2 ** b) != 0:
                if bit_count_ideal[b] % 2 == 1:
                    if new_count[b] + 1 >= 2:
                        done = True
                        break
                    else:
                        new_count[b] += 1
                else:
                    if new_count[b] + 1 >= 1:
                        done = True
                        break
                    else:
                        new_count[b] += 1
        if done:
            break
        bit_count = new_count
        j -= 1
    mini = j - i + 1
    mini_pair = (i+1, j+1)

    for k in range(i-1, -1, -1):
        for b in range(31):
            if arr[k] & (2 ** b) != 0:
                bit_count[b] -= 1
        
        done = False
        while j >= k:
            new_count = bit_count[:]
            for b in range(31):
                if arr[j] & (2 ** b) != 0:
                    if bit_count_ideal[b] % 2 == 1:
                        if new_count[b] + 1 >= 2:
                            done = True
                            break
                        else:
                            new_count[b] += 1
                    else:
                        if new_count[b] + 1 >= 1:
                            done = True
                            break
                        else:
                            new_count[b] += 1
            if done:
                break
            bit_count= new_count
            j -= 1
        if j - (k-1) < mini:
            mini = j - (k-1)
            mini_pair = (k+1, j+1)
    if mini == 0:
        print(1, 1)
    else:
        print(mini_pair[0], mini_pair[1])
                

for t in range(int(input())):
    solve()