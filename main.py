class Node:
    def __init__(self, environment: list, last_move: str = None, state: str = "n", parent = None, cost : int = 0, depth :int =0 ):
        self.environment = environment
        self.parent = parent
        self.state = state
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
# def fill_node_cost(location :tuple):
#     return int(environment[location[0]][location[1]][0])
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
# def generate_children(node : Node):
#     children = []
#     up = (node.location[0]-1, node.location[1])
#     down = (node.location[0]+1, node.location[1])
#     left = (node.location[0], node.location[1]-1)
#     right = (node.location[0], node.location[1]+1)
#     if(up[0]>=0 and up[0]< x and up[1]>= 0 and up[1]< y):
#         if(not(up in forbidden_location)):
#             children.append(Node(up,"u",fill_node_state(up),node,fill_node_cost(up)))
#
#     if (down[0] >= 0 and down[0] < x and down[1] >= 0 and down[1] < y):
#         if (not (down in forbidden_location)):
#             children.append(Node(down,"d",fill_node_state(down),node,fill_node_cost(down)))
#
#     if (left[0] >= 0 and left[0] < x and left[1] >= 0 and left[1] < y):
#         if (not (left in forbidden_location)):
#             children.append(Node(left,"l",fill_node_state(left),node,fill_node_cost(left)))
#
#     if (right[0] >= 0 and right[0] < x and right[1] >= 0 and right[1] < y):
#         if (not (right in forbidden_location)):
#             children.append(Node(right,"r",fill_node_state(right),node,fill_node_cost(right)))
#     return children




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


start=Node(environment,None,"n",None,0)
print(start.environment[0])
# IDS(start,4)




# print(start.cost)
# ch=generate_children(start)
#
#
# print(robot_location)
# print(butter_location)
# print(goal_location)
# print(forbidden_location)
# print(environment)
