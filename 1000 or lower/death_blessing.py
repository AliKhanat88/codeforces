def main():
    t = int(input())
    for i in range(t):
        length = int(input())
        
        healths = list(map(int, input().split()))
        magics = list(map(int, input().split()))
        seconds = healths[0]
        maxi = 0
        for i in range(1, length):
            if magics[maxi] < magics[i]:
                maxi = i
            seconds += healths[i]
        magics.pop(maxi)
        seconds += sum(magics)
        print(seconds)
main()