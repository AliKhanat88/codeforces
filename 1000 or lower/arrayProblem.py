def check_max_sum(n, arr):
    i = 1
    sum = arr[0]
    result = 0
    first_dip = -1
    while i < n:
        if i == n -1 and arr[i] < arr[i-1]:
            
            if first_dip == -1 and arr[i-1] > arr[i]:
                first_dip = i-1
                # sum -= arr[i - 1]
                result -= arr[n-2]
            diff_index = i - first_dip
            result += arr[n-2]
            if (diff_index) * (arr[first_dip]) > (result + (diff_index+2) * arr[i]):
                sum += (diff_index + 1) * (arr[first_dip] - arr[i]) - arr[first_dip]
            else:
                sum += result + arr[i] 
        elif arr[i-1] <= arr[i]:
            sum += arr[i]
            if first_dip != -1:
                diff_index = i - 1 - first_dip
                if (diff_index) * (arr[first_dip]) > (result + (diff_index+2) * arr[i-1]):
                    sum += (diff_index + 1) * (arr[first_dip] - arr[i-1]) - arr[first_dip]
                else:
                    sum += result + arr[i-1] 
            first_dip = -1

        else:
            if first_dip == -1:
                first_dip = i - 1
                result = 0
            result += arr[i]
        i = i + 1 
       
    print(sum)       



def main():
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        check_max_sum(n, arr)


main()