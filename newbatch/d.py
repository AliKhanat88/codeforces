import math
m = 400001
def getprimes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    prime = [True for _ in range(n+1)]
    p = 2

    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p + p, n+1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    prime_numbers = [p for p in range(2, n+1) if prime[p]]
    return prime_numbers

primes = getprimes(m)

def solve():
    n = int(input())
    ans = [-1] * (n+1)
    for i in range(1, n+1):
        if ans[i] == -1:
            start = 2
            ans[i] = 1
            for j in range(len(primes)):
                if i ^ primes[j] <= n and i ^ primes[j] != 0 and ans[i ^ primes[j]] == -1:
                    ans[i ^ primes[j]] = start 
                    start += 1
    print(max(ans))
    print(*ans[1:])
            
            

for t in range(int(input())):
    solve()