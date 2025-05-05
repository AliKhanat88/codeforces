def main():
    n , m = map(int, input().split())
    world_map = [int(num) for num in input().split()]
    pos_positive = [0] * n
    sum = 0
    for i in range(1 ,n):
        if world_map[i] < world_map[i-1]:
            sum += world_map[i-1] - world_map[i]
            pos_positive[i] = sum
        else:
            pos_positive[i] = sum
    for l in range(m):
        i , j = map(int, input().split())
        if i > j:
            sum = pos_positive[i-1] - pos_positive[j-1]
            sum  = (world_map[j-1] - world_map[i-1]) - sum 
            sum = - sum
        else:
            sum = pos_positive[j-1] - pos_positive[i-1]
        print(sum)

main()