from collections import defaultdict



def solve():
    n, m = map(int, input().split())

    arr = list(map( int, input().split()))
    c = [0] * (2 * m + 2)
    def get_index(x):
        return x + m
    for i in range(n):
        c[get_index(arr[i])] += 1
    
    
    c[get_index(0)] = 0
    
    maxi = defaultdict(lambda:0)
    count = 0
    temp_maxi = 0
    for i in range(n):
        # print(c)
        if arr[i] == 0:
            count += 1
            framei = -count
            maxi[str((-count, 0))] = maxi[str((-count + 1, 0))] + c[get_index(-count)]
            temp_maxi = max(temp_maxi, maxi[str((-count, 0))])
            maxi[str((0, count))] = maxi[str((0, count - 1))] + c[get_index(count)]
            temp_maxi = max(temp_maxi, maxi[str((0, count))])
            for framej in range(1, count):
                framei += 1
                maxi[str((framei, framej))] = max(maxi[str((framei + 1, framej))] + c[get_index(framei)], maxi[str((framei, framej - 1))] + c[get_index(framej)])
                temp_maxi = max(temp_maxi, maxi[str((framei, framej))])
                
        else:
            c[get_index(arr[i])] -= 1
    # print(maxi)
    # print(max(maxi))
    print(temp_maxi)
solve()
    