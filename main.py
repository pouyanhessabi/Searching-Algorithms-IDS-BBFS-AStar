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
queue = []
tree=[]
robot_location=(0,0)
butter_location=[]
goal_location=[]
forbidden_location=[]

def generate_children(node : Node):
    children = []
    up = (node.location[0]-1, node.location[1])
    down = (node.location[0]+1, node.location[1])
    left = (node.location[0], node.location[1]-1)
    right = (node.location[0], node.location[1]+1)
    if(up[0]>=0 and up[0]< x and up[1]>= 0 and up[1]< y):
        if(not(up in forbidden_location)):
            children.append(up)

    if (down[0] >= 0 and down[0] < x and down[1] >= 0 and down[1] < y):
        if (not (down in forbidden_location)):
            children.append(down)

    if (left[0] >= 0 and left[0] < x and left[1] >= 0 and left[1] < y):
        if (not (left in forbidden_location)):
            children.append(left)

    if (right[0] >= 0 and right[0] < x and right[1] >= 0 and right[1] < y):
        if (not (right in forbidden_location)):
            children.append(right)
    print(len(children))




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



# for limit in range((x*y)):

stat=Node(robot_location)
generate_children(stat)

print(robot_location)
print(butter_location)
print(goal_location)
print(forbidden_location)
print(environment)
