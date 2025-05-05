# Initializing Array
data = [[1 , 6 , 8 , 4 , 5],
        [5, 7, 2, 3, 9],
        [9, 3, 4, 6, 2],
        [8, 2, 9, 7, 4]]

# Taking input 
sum = int(input())

# defining the Dfs function
def dfs(i, j):
    temp_maxi = 0

    # Defining start for the dfs
    stack = [(i, j, 0, 0, -1)]

    # Array for saving the path
    path = [-1]

    # loop for dfs
    while len(stack):
        cur = stack.pop()

        # Checking wethe the points are in the grid or not
        if cur[0] >= 0 and cur[0] < len(data) and cur[1] >= 0 and cur[1] < len(data[0]): 
            if cur[2] + data[cur[0]][cur[1]] <= sum:
                
                # loop for correcting the current path
                while cur[4] != path[-1]:
                    path.pop()

                # if the point is already visited breaking out of it
                if (cur[0], cur[1]) in path:
                    continue

                # appending in the path
                path.append((cur[0], cur[1]))
                
                # going to the points neigbors
                temp_maxi = max(temp_maxi, cur[3] + 1)
                neigbors = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

                # savinf every neigbor in the stack
                for ne in neigbors:
                    stack.append((cur[0] + ne[0], cur[1] + ne[1], cur[2] + data[cur[0]][cur[1]], cur[3] + 1, (cur[0], cur[1])))
    return temp_maxi

# getting the max path length
maxi = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        
        # calling dfs function for every point
        maxi = max(maxi, dfs(i, j))


print(maxi)          
        
