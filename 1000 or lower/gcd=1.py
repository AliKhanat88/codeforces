def combinatiton(arr, r, result):
    n = len(arr)
    all_combinations = []
    combination_at_index(arr,r, 0,n, [], result, all_combinations)
    print(all_combinations)

def combination_at_index(arr, r,index, n, temp_arr, result, all_combinations):
    if index >= n:
        return
    if r == 1:
        for i in range(index, n):
            if sum(temp_arr) + arr[i] == result:
                temp_arr.append(arr[i])
                all_combinations.append([*temp_arr])
                temp_arr.pop(-1)
    else:
        for j in range(index, n):
            temp_arr.append(arr[j])
            combination_at_index(arr, r-1,index+1,n,temp_arr, result, all_combinations)
            temp_arr.pop(-1)
            index += 1




def check_gcd_one(arr, n):
    temp = arr[0]
    for i in  range(1, n):
        temp =  gcd(temp, arr[i])
    if temp == 1:
        return True
    return False

def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)


def compute_less_dist(n , arr):
    if check_gcd_one(arr, n):
        print(0)
        return
    for i in range(n-1, -1, -1):
        new = gcd(arr[i], i+1)
        temp = [*arr]
        temp[i] = new
        if check_gcd_one(temp, n):
            print(n-i)
            return

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        compute_less_dist(n , arr)

main()