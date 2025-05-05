
dict = {}
nums = [1, 1, 2, 3, 4, 5, 4, 5, 4, 5, 5]
ans = []
for num in nums:
    if num in dict:
        dict[num] += 1
    else:
        ans.append(num)
        dict[num] = 1
print(dict)
maxi = -1
maxi_val = None
for key, val in dict.items():
    if val > maxi:
        maxi = val
        maxi_val = key


print(f"Element with most occorance is {maxi_val} with count {maxi}")
print(ans)