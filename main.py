
environment=[]
robot_location=(0,0)
butter_location=[]
goal_location=[]
forbidden_location=[]
x,y= map(int, input().split())
for i in range(x):
    environment.append(input().split())
for i in range(x):
    for j in range(y):
        if (environment[i][j].find('r') != -1):
            robot_location=(i,j)
        elif (environment[i][j].find('b') != -1):
            butter_location.append((i,j))
        elif (environment[i][j].find('p') != -1):
            goal_location.append((i,j))
        elif (environment[i][j].find('x') != -1):
            forbidden_location.append((i,j))


print(robot_location)
print(butter_location)
print(goal_location)
print(forbidden_location)

print(environment)
