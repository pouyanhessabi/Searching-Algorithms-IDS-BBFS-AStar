import sys

sys.setrecursionlimit(5000)


class Node:
    def __init__(self, robot_loc: tuple, butter_loc: list, last_move: str = None, parent=None, cost: int = 0,
                 depth: int = 0):
        self.robot_loc = robot_loc
        self.butter_loc = butter_loc
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
explored = []
robot_location = (0, 0)
butter_location = []
goal_location = []
forbidden_location = []
path = []
final_cost = 0
final_depth = 0
x = 0
y = 0


def read_from_file(file_name: str):
    global x, y, robot_location
    f = open(file_name, "r")
    x, y = map(int, f.readline().split())
    for i in range(x):
        environment.append(f.readline().split())
    for i in range(x):
        for j in range(y):
            if (environment[i][j].find('r') != -1):
                robot_location = (i, j)
            elif (environment[i][j].find('b') != -1):
                butter_location.append((i, j))
            elif (environment[i][j].find('p') != -1):
                goal_location.append((i, j))
            elif (environment[i][j].find('x') != -1):
                forbidden_location.append((i, j))


def write_on_file(file_name):
    f = open(file_name, "w")
    for i in range(len(path), 0, -1):
        f.write(path[i - 1] + " ")
    f.write("\n")
    f.write(str(final_cost) + "\n")
    f.write(str(final_depth) + "\n")


def get_path(node: Node):
    nd = node
    if (nd.depth == 0):
        return
    else:
        path.append(nd.last_move)
        nd = nd.parent
        get_path(nd)


def fill_node_cost(location: tuple):
    return int(environment[location[0]][location[1]][0])


def check_goal(node: Node):
    global final_cost, final_depth
    for i in range(len(node.butter_loc)):
        if (node.butter_loc[i] in goal_location):
            goal_location.remove(node.butter_loc[i])
            node.butter_loc.remove(node.butter_loc[i])
            if (len(goal_location) == 0):
                get_path(node)
                final_cost = node.cost
                final_depth = node.depth
            return node
    return None


def DLS(maxDepth):
    if (len(frontier) == 0 and len(explored) != 0):
        return
    else:
        nd = frontier.pop()
        explored.append(nd)
        ch = generate_children(nd)
        for i in range(len(ch)):
            condition = True
            if (ch[i].depth <= maxDepth):
                for j in range(len(explored)):
                    if (ch[i].robot_loc == explored[j].robot_loc and set(ch[i].butter_loc) == set(
                            explored[j].butter_loc)):
                        if (ch[i].cost < explored[j].cost):
                            explored.pop(j)
                        else:
                            condition = False
                        break
                if (condition):
                    frontier.append(ch[i])
        DLS(maxDepth)


def IDS(root: Node):
    end = False
    i = 0
    while (True):
        explored.clear()
        frontier.append(root)
        DLS(i)
        for j in range(len(explored)):
            new_root = check_goal(explored[j])
            if (new_root != None):
                root = new_root

                if (len(goal_location) > 0):
                    IDS(new_root)
                    end = True
                    break
                else:
                    end = True
        i += 1
        if (i >= 100):
            break
        if end == True:
            break


def generate_children(node: Node):
    children = []
    robot_neighbors = []
    neighbor_butter_location = []

    up = (node.robot_loc[0] - 1, node.robot_loc[1])
    robot_neighbors.append(up)
    down = (node.robot_loc[0] + 1, node.robot_loc[1])
    robot_neighbors.append(down)
    left = (node.robot_loc[0], node.robot_loc[1] - 1)
    robot_neighbors.append(left)
    right = (node.robot_loc[0], node.robot_loc[1] + 1)
    robot_neighbors.append(right)
    for i in range(4):
        for j in range(len(node.butter_loc)):
            if (robot_neighbors[i] == node.butter_loc[j]):
                neighbor_butter_location.append(robot_neighbors[i])

    if (up[0] >= 0 and up[0] < x and up[1] >= 0 and up[1] < y):
        if (not (up in forbidden_location)):
            if (not (up in neighbor_butter_location)):
                children.append(Node(up, node.butter_loc, "u", node, fill_node_cost(up)))

    if (down[0] >= 0 and down[0] < x and down[1] >= 0 and down[1] < y):
        if (not (down in forbidden_location)):
            if (not (down in neighbor_butter_location)):
                children.append(Node(down, node.butter_loc, "d", node, fill_node_cost(down)))

    if (left[0] >= 0 and left[0] < x and left[1] >= 0 and left[1] < y):
        if (not (left in forbidden_location)):
            if (not (left in neighbor_butter_location)):
                children.append(Node(left, node.butter_loc, "l", node, fill_node_cost(left)))

    if (right[0] >= 0 and right[0] < x and right[1] >= 0 and right[1] < y):
        if (not (right in forbidden_location)):
            if (not (right in neighbor_butter_location)):
                children.append(Node(right, node.butter_loc, "r", node, fill_node_cost(right)))

    if (len(neighbor_butter_location) != 0):
        for i in neighbor_butter_location:
            if (i == up):
                b_loc = (up[0] - 1, up[1])
                action = "u"
            elif (i == down):
                b_loc = (down[0] + 1, down[1])
                action = "d"
            elif (i == left):
                b_loc = (left[0], left[1] - 1)
                action = "l"
            elif (i == right):
                action = "r"
                b_loc = (right[0], right[1] + 1)
            if (b_loc[0] >= 0 and b_loc[0] < x and b_loc[1] >= 0 and b_loc[1] < y):
                if (not (b_loc in forbidden_location) and not (b_loc in node.butter_loc)):
                    temp = node.butter_loc.copy()
                    temp.remove(i)
                    temp.append(b_loc)
                    children.append(Node(i, temp, action, node, fill_node_cost(i)))
    return children


file_name = input() + ".txt"

read_from_file(file_name)
start = Node(robot_location, butter_location, None, None, 0)
IDS(start)
write_on_file("result" + file_name[4] + ".txt")

# if (len(goal_location) == 0):
#     print(path)
# else:
#     print("can’t pass the butter")
