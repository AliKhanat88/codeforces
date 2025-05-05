def print_remainder(rem):
    if rem > 8 and rem < 11:
        return 25
    elif rem > 6 and rem < 9:
        return 20
    elif rem > 0 and rem < 7:
        return 15
    elif rem == 0: return 0 
    return 1000000
def main():
    for t in range(int(input())):
        n = int(input())
        t1 = (n // 10) * 25 + print_remainder(n%10)
        t2 = (n // 8) * 20 + print_remainder(n%8)
        if n >= 8:
            t3 = (n // 8 - 1) * 20 + print_remainder(n % 8 + 8)
        else:
            t3 = 10e16
        t4 = (n // 6) * 15 + print_remainder(n%6)
        if n > 6:
            t5 = (n // 6 - 1) * 15 + print_remainder(n%6 + 6)
        else:
            t5 = 10e16
        print(min(t1,t2,t3, t4, t5))

main()