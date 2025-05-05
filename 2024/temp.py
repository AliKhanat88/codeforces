from ttemp import main
from adjustTthePresentation import solve
from random import randint

n = 5
m = 5
q = 10
for i in range(10000):
    arr1 = [i+1 for i in range(n)]
    brr1 = [randint(1, n) for i in range(m)]
    queries = []
    for i in range(q):
        queries.append((randint(1, m),randint(1, n)))
    arr2 = arr1[:]
    brr2 = brr1[:]
    brr3 = brr1[:]
    temp1 = solve(n,m,q,arr1,brr1,queries)
    temp2 = main(n,m,q,arr2,brr2,queries)
    if temp1 != temp2:
        print("Found")
        print(temp1)
        print(temp2)
        print(arr1)
        print(brr3)
        print(queries)
        break
    else:
        print("hey")
    # f1.close()
    # f2.close()