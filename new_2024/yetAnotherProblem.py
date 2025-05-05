from collections import defaultdict
import sys
input= sys.stdin.readline
from bisect import bisect_left

def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    dict = defaultdict(lambda: [])
    xor = 0
    xor_arr = [0] * (n+1)
    dict[0].append(0)
    
    even = defaultdict(lambda: [])
    odd = defaultdict(lambda: [])
    even[0].append(0)
    for i in range(n):
        xor = xor ^ arr[i]
        xor_arr[i+1] = xor
        dict[xor].append(i+1)
        if (i+1) % 2 == 0:
            even[xor].append(i+1)
        else:
            odd[xor].append(i+1)
    # print(xor_arr)
    # print(dict)
    # print(even)
    # print(odd)
    
    for i in range(q):
        a, b = map(int, input().split())
        a -= 1
        # print(a, b, i)
        if (b - a + 2) % 2 == 1:
            
            index_b = bisect_left(dict[xor_arr[a]], b)
            index_a = bisect_left(dict[xor_arr[a]], a)
            # print(index_a, index_b)
            if index_b < len(dict[xor_arr[a]]) and dict[xor_arr[a]][index_b] == b:
                if index_b - index_a >= b - a:
                    print(0)
                else:
                    print(1)
            else:
                print(-1)
        else:
            index_b = bisect_left(dict[xor_arr[a]], b)
            index_a = bisect_left(dict[xor_arr[a]], a)
            # print(index_a, index_b)
            if index_b < len(dict[xor_arr[a]]) and dict[xor_arr[a]][index_b] == b:
                if index_b - index_a >= b - a:
                    print(0)
                else:
                    if arr[a] == 0 or arr[b-1] == 0:
                        print(1)

                    else:
                        if a % 2 == 1:
                            index = bisect_left(even[xor_arr[a]], a)
                            if len(even[xor_arr[a]]) > index and even[xor_arr[a]][index] < b:
                                print(2)
                                continue
                        else:
                            index = bisect_left(odd[xor_arr[a]], a)
                            if len(odd[xor_arr[a]]) > index and odd[xor_arr[a]][index] < b:
                                print(2)
                                continue 
                            
                        print(-1)

            else:
                print(-1)

 

solve()
