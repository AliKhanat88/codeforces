# from bisect import bisect_right


# a = [1,2,3,4,5,6]

# print(bisect_right(a, 4, 2,3))

# print(set(set("1231")))
# arr = [13, 1, 4, 7, 12, 2, 5, 8, 11, 3, 6, 9, 10]
# sum_arr = [0] * 13
# sum_arr = arr[0]
# for i in range(1, 13):
#     sum_arr[i] = sum_arr[i-1] + arr

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# temp_arr = [0] * 1000001
# for i in range(1, 1000001):
#     if len(set(str(i))) == len(str(i)):
#         temp_arr[i] = temp_arr[i-1] + 1 
#     else:
#         temp_arr[i] = temp_arr[i-1]
# # Complete the countNumbers function below.
# def countNumbers(arr):
#     for query in arr:
#         print(temp_arr[query[1]] - temp_arr[query[0]-1])

# if __name__ == '__main__':



import requests

def get_codeforces_problems_by_rating(rating):
    api_url = f"https://codeforces.com/api/problemset.problems?tags={rating}-rated"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200 and data['status'] == 'OK':
            problems = data['result']['problems']
            return problems
        else:
            print(f"Error: {data['comment']}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example: Get problems with a rating of 1500
rating = 1500
problems = get_codeforces_problems_by_rating(rating)

if problems:
    print(f"Problems with {rating} rating:")
    for problem in problems:
        print(problem['name'], problem['contestId'], problem['index'])
else:
    print("Failed to fetch problems.")
