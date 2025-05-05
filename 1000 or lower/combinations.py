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
