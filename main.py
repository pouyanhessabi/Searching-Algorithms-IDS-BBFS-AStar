class Node:
    def __init__(self, location: tuple, last_move: str = None, parent = None, depth: int = 0):
        self.location = location
        self.parent = parent
        self.last_move = last_move
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0






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
# stat=Node(robot_location,"u")
# print(stat.location)
print(butter_location)
print(goal_location)
print(forbidden_location)
print(environment)
