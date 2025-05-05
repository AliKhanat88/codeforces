n, x0 = map(int, input().split())
t_x, t_y = map(int, input().split())
x = min(t_x,t_y)
y = max(t_x, t_y)
for i in range(n-1):
    x_n, y_n = map(int, input().split())
    mini = min(x_n, y_n)
    maxi = max(x_n, y_n)
    x = max(mini, x)
    y = min(maxi, y)
if y - x < 0:
    print(-1)
else:
    if x0 >= x and x0 <= y:
        print(0)
    else:
        print(min(abs(x-x0), abs(y-x0)))
        
    