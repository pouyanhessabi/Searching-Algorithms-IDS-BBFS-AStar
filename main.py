class Node:
    def __init__(self,robot_loc: tuple, butter_loc: list, last_move: str = None, parent = None, cost : int = 0, depth :int =0 ):
        self.robot_loc = robot_loc
        self.butter_loc=butter_loc
        self.parent = parent
        self.last_move = last_move
        if parent:
            self.cost = parent.cost + cost
            self.depth = parent.depth + 1
        else:
            self.cost = cost
            self.depth = 0

environment = []
frontier = []
tree = []
robot_location=(0,0)
butter_location = []
goal_location = []
forbidden_location=[]
# def fill_node_state(location :tuple):
#     if(location in butter_location):
#         return "b"
#     elif (location in goal_location):
#         return "p"
#     else:
#         return "n"
#
def fill_node_cost(location :tuple):
    return int(environment[location[0]][location[1]][0])
#
#
# def DFS(node : Node,maxDepth):
#     if(len(frontier)==0 and len(tree) != 0 ):
#         return
#     else:
#         nd = frontier.pop()
#         tree.append(nd)
#         ch=generate_children(nd)
#         for i in range(len(ch)):
#             condition=True
#             # print(ch[i].location," childerenn")
#             if(ch[i].depth<=maxDepth):
#                 for j in range(len(tree)):
#                     if (ch[i].location == tree[j].location ):
#                         if(ch[i].cost < tree[j].cost):
#                             tree.pop(j)
#                         else:
#                             condition = False
#                         break
#                 if (condition):
#                     print("yeeeeeeee")
#                     frontier.append(ch[i])
#         # print("___________________")
#         # for i in range(len(frontier)):
#         #     print(frontier[i].location, "frontier", maxDepth,node.location)
#         # print("___________________________")
#         DFS(nd,maxDepth)
#
#
#
# def IDS(root : Node, limit):
#     for i in range(limit):
#         tree.clear()
#         frontier.append(root)
#         DFS(root,i)
#         for i in range(len(tree)):
#             print(tree[i].location)
#         print("________________")
#
def generate_children(node : Node):
    children = []
    robot_neighbors=[]
    neighbor_butter_location=[]

    up = (node.robot_loc[0]-1, node.robot_loc[1])
    robot_neighbors.append(up)
    down = (node.robot_loc[0]+1, node.robot_loc[1])
    robot_neighbors.append(down)
    left = (node.robot_loc[0], node.robot_loc[1]-1)
    robot_neighbors.append(left)
    right = (node.robot_loc[0], node.robot_loc[1]+1)
    robot_neighbors.append(right)
    for i in range(4):
        for j in range(len(node.butter_loc)):
            if (robot_neighbors[i]==node.butter_loc[j]):
                neighbor_butter_location.append(robot_neighbors[i])


    if(up[0]>=0 and up[0]< x and up[1]>= 0 and up[1]< y):
        if(not(up in forbidden_location)):
            if(not (up in neighbor_butter_location)):
                children.append(Node(up,node.butter_loc,"u",node,fill_node_cost(up)))

    if (down[0] >= 0 and down[0] < x and down[1] >= 0 and down[1] < y):
        if (not (down in forbidden_location)):
            if (not (down in neighbor_butter_location)):

                children.append(Node(down,node.butter_loc,"d",node,fill_node_cost(down)))

    if (left[0] >= 0 and left[0] < x and left[1] >= 0 and left[1] < y):
        if (not (left in forbidden_location)):
            if (not (left in neighbor_butter_location)):
                children.append(Node(left,node.butter_loc,"l",node,fill_node_cost(left)))

    if (right[0] >= 0 and right[0] < x and right[1] >= 0 and right[1] < y):
        if (not (right in forbidden_location)):
            if (not (right in neighbor_butter_location)):
                children.append(Node(right,node.butter_loc,"r",node,fill_node_cost(right)))


    if(len(neighbor_butter_location)!=0):
        for i in neighbor_butter_location:
            if (i == up):
                b_loc=(up[0]-1, up[1])
                action="u"
            elif (i == down):
                b_loc=(down+1, down[1])
                action="d"
            elif (i == left):
                b_loc= (left[0], left[1]-1)
                action="l"
            elif (i == right):
                action="r"
                b_loc=(right[0], right[1]+1)
            if (b_loc[0] >= 0 and b_loc[0] < x and b_loc[1] >= 0 and b_loc[1] < y):
                if (not (b_loc in forbidden_location) and not (b_loc in node.butter_loc)):
                        temp=node.butter_loc.copy()
                        temp.remove(i)
                        temp.append(b_loc)
                        children.append(Node(i, temp, action, node, fill_node_cost(i)))
    return children




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



# for limit in range(1,(x*y)):


start=Node(robot_location,butter_location,None,None,int(environment[robot_location[0]][robot_location[1]][0]))
ch=generate_children(start)
for i in range (len(ch)):
    print(ch[i].butter_loc,ch[i].robot_loc,ch[i].cost)

# IDS(start,4)




# print(start.cost)
#
#
# print(robot_location)
# print(butter_location)
# print(goal_location)
# print(forbidden_location)
# print(environment)
