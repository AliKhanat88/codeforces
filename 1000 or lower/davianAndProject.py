from collections import defaultdict

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input().split()
        visit = {}
        j = 0
        for num in s:
            visit[j] = int(num)
            j = j + 1
        sorted_visit = sorted(visit.items(), key=lambda x: x[1], reverse=True)
        dist = 0
        position_wise = {}
        k = 1
        for j in range(0, n, 2):
            position_wise[sorted_visit[j][0]] = k
            dist += 2 * (sorted_visit[j][1] * k)
            k += 1
        k = -1
        for j in range(1, n, 2):
            position_wise[sorted_visit[j][0]] = k
            dist += 2 * (sorted_visit[j][1] * abs(k))
            k -= 1
        print(dist)
        print(0, end=" ")
        for j in range(n):
            print(position_wise[j], end=" ")
        print()


main() 
        
        
