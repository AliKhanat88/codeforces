
# set for saving the permutations
ans = set()

# recursive function for the starting stone
def recur(main, sumi, i = 0, start = 1, cur = []):
    
    # base case
    if i == 2:
        if sumi + start > main:
            return

        for temp in range(start, 21):
            if temp + sumi == main:
                ans.add(tuple(cur[:] + [temp]))

    elif i > 2:
        return
    else:
        # Entering into next recursive call
        for temp in range(start, 21):
            recur(main, sumi+start, i+1, temp, cur[:] + [start])

# input of the total sum
sumi = int(input())

# Calling recursive function for every stone
for i in range(1, 21):
    recur(sumi, 0, 0, i)

# Sorting the points 
new_ans = []
for temp in ans:
    new_ans.append(tuple(sorted(list(temp))))

new_ans.sort()

# Printing the answer
for temp in new_ans:
    print(", ".join(str(num) for num in tuple(sorted(list(temp)))))