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


class NodeForGoal:
    def __init__(self, goal_loc: list, last_move: str = None, parent=None,
                 cost: int = 0,
                 depth: int = 0):
        self.goal_loc = goal_loc
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
visited = []
tree = []
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
            if environment[i][j].find('r') != -1:
                robot_location = (i, j)
            elif environment[i][j].find('b') != -1:
                butter_location.append((i, j))
            elif environment[i][j].find('p') != -1:
                goal_location.append((i, j))
            elif environment[i][j].find('x') != -1:
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
    if nd.depth == 0:
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
        if node.butter_loc[i] in goal_location:
            # print(node.butter_loc[i])
            # print(node.parent.butter_loc)
            goal_location.remove(node.butter_loc[i])
            node.butter_loc.remove(node.butter_loc[i])
            if len(goal_location) == 0:
                get_path(node)
                final_cost = node.cost
                final_depth = node.depth

            # start = Node(node.robot_loc, node., None, None,node.cost)
            return node
    return None


def BFS_for_robot(root: Node):
    # frontier.append(root)
    if len(frontier) == 0 and len(tree) != 0:
        return
    for i in range(len(goal_location)):
        if root.butter_loc == goal_location[i]:
            break

    else:
        tmp_check = True
        for i in range(len(frontier)):
            for j in range(len(frontier)):
                if i == j:
                    break
                if tmp_check and frontier[i].robot_loc == frontier[j].robot_loc and frontier[i].depth == frontier[
                    j].depth and \
                        frontier[i].butter_loc == frontier[j].butter_loc:
                    frontier.pop(i)
                    tmp_check = False
                    break
        nd = frontier.pop(0)
        tree.append(nd)
        # tree.append(nd)
        ch = generate_children(nd)
        for i in range(len(ch)):
            condition = True
            # if ch[i].depth <= 1000:
            for j in range(len(tree)):
                if ch[i].robot_loc == tree[j].robot_loc and set(ch[i].butter_loc) == set(tree[j].butter_loc):
                    if ch[i].cost < tree[j].cost:
                        tree.pop(j)
                        pass
                    else:
                        condition = False
                    break
            if condition:
                # print("yeeeeeeee", ch[i].robot_loc)
                frontier.append(ch[i])

        print("___________________")
        # print("z" , frontier[0].robot_loc)
        # print("___________________________")
        print(nd.robot_loc, nd.depth, nd.butter_loc, nd.last_move)

        BFS_for_robot(nd)


def bid():
    for i in range(len(goal_location)):
        BFS_for_robot()


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
            if robot_neighbors[i] == node.butter_loc[j]:
                neighbor_butter_location.append(robot_neighbors[i])

    if 0 <= up[0] < x and 0 <= up[1] < y:
        if not (up in forbidden_location):
            if not (up in neighbor_butter_location):
                children.append(Node(up, node.butter_loc, "u", node, fill_node_cost(up)))

    if 0 <= down[0] < x and down[1] >= 0 and down[1] < y:
        if not (down in forbidden_location):
            if not (down in neighbor_butter_location):
                children.append(Node(down, node.butter_loc, "d", node, fill_node_cost(down)))

    if left[0] >= 0 and left[0] < x and left[1] >= 0 and left[1] < y:
        if not (left in forbidden_location):
            if not (left in neighbor_butter_location):
                children.append(Node(left, node.butter_loc, "l", node, fill_node_cost(left)))

    if right[0] >= 0 and right[0] < x and right[1] >= 0 and right[1] < y:
        if not (right in forbidden_location):
            if not (right in neighbor_butter_location):
                children.append(Node(right, node.butter_loc, "r", node, fill_node_cost(right)))

    if len(neighbor_butter_location) != 0:
        for i in neighbor_butter_location:
            if i == up:
                b_loc = (up[0] - 1, up[1])
                action = "u"
            elif i == down:
                b_loc = (down[0] + 1, down[1])
                action = "d"
            elif i == left:
                b_loc = (left[0], left[1] - 1)
                action = "l"
            elif i == right:
                action = "r"
                b_loc = (right[0], right[1] + 1)
            if b_loc[0] >= 0 and b_loc[0] < x and b_loc[1] >= 0 and b_loc[1] < y:
                if not (b_loc in forbidden_location) and not (b_loc in node.butter_loc):
                    temp = node.butter_loc.copy()
                    temp.remove(i)
                    temp.append(b_loc)
                    children.append(Node(i, temp, action, node, fill_node_cost(i)))
    return children


def generate_goal_children(node: NodeForGoal, index: int):
    goal_children = []
    goal_neighbors = []
    up = (node.goal_loc[index][0], node.goal_loc[index][1])
    goal_neighbors.append(up)

    down = (node.goal_loc[index][0] + 1, node.goal_loc[index][1])
    goal_neighbors.append(down)
    left = (node.goal_loc[index][0], node.goal_loc[index][1] - 1)
    goal_neighbors.append(left)
    right = (node.goal_loc[index][0], node.goal_loc[index][1] + 1)
    goal_neighbors.append(right)

    # for i in range(4):
    #     for j in range(len(butter_location)):
    #         if goal_neighbors[i] == butter_location[j]:
    #             butter_up = (butter_location[0] - 1, butter_location[1])
    #             butter_down = (butter_location[0] + 1, butter_location[1])
    #             butter_left = (butter_location[0], butter_location[1] - 1)
    #             butter_right = (butter_location[0], butter_location[1] + 1)
    #             if robot_location == butter_up or robot_location == butter_down or robot_location == butter_left or robot_location == butter_right:
    #                 print("resid")
    #                 return

    # else:

    if 0 <= up[0] < x and 0 <= up[1] < y:
        if not (up in forbidden_location):
            temp = node.goal_loc.copy()
            temp.remove(node.goal_loc[index])
            temp.append(up)
            goal_children.append(NodeForGoal(temp, "u", node, fill_node_cost(up)))

    if 0 <= up[0] < x and 0 <= up[1] < y:
        if not (up in forbidden_location):
            temp = node.goal_loc.copy()
            temp.remove(node.goal_loc[index])
            temp.append(up)
            goal_children.append(NodeForGoal(temp, "u", node, fill_node_cost(up)))

    if 0 <= up[0] < x and 0 <= up[1] < y:
        if not (up in forbidden_location):
            temp = node.goal_loc.copy()
            temp.remove(node.goal_loc[index])
            temp.append(up)
            goal_children.append(NodeForGoal(temp, "u", node, fill_node_cost(up)))

    if 0 <= up[0] < x and 0 <= up[1] < y:
        if not (up in forbidden_location):
            temp = node.goal_loc.copy()
            temp.remove(node.goal_loc[index])
            temp.append(up)
            goal_children.append(NodeForGoal(temp, "u", node, fill_node_cost(up)))
    #
    #
    # if 0 <= down[0] < x and 0 <= down[1] < y:
    #     if not (down in forbidden_location):
    #         goal_children.append(NodeForGoal(down, node.butter_loc, node.goal_loc, "d", node, fill_node_cost(down)))
    #
    # if 0 <= left[0] < x and 0 <= left[1] < y:
    #     if not (left in forbidden_location):
    #         goal_children.append(NodeForGoal(left, node.butter_loc, node.goal_loc, "l", node, fill_node_cost(left)))
    #
    # if 0 <= right[0] < x and 0 <= right[1] < y:
    #     if not (left in forbidden_location):
    #         goal_children.append(NodeForGoal(right, node.butter_loc, "r", node.goal_loc, fill_node_cost(left)))

    # if len(neighbor_butter_location) != 0:
    #     for i in neighbor_butter_location:
    #         if i == up:
    #             b_loc = (up[0] - 1, up[1])
    #             action = "u"
    #         elif i == down:
    #             b_loc = (down[0] + 1, down[1])
    #             action = "d"
    #         elif i == left:
    #             b_loc = (left[0], left[1] - 1)
    #             action = "l"
    #         elif i == right:
    #             action = "r"
    #             b_loc = (right[0], right[1] + 1)
    # if b_loc[0] >= 0 and b_loc[0] < x and b_loc[1] >= 0 and b_loc[1] < y:
    #     if not (b_loc in forbidden_location) and not (b_loc in node.butter_loc):
    #         temp = node.butter_loc.copy()
    #         temp.remove(i)
    #         temp.append(b_loc)
    #         children.append(Node(i, temp, action, node, fill_node_cost(i)))
    return goal_children


# for limit in range(1,(x*y)):
# file_name = input() + ".txt"
file_name = "test1.txt"
read_from_file(file_name)
start = Node(robot_location, butter_location, None, None, int(environment[robot_location[0]][robot_location[1]][0]))
# purpose = NodeForGoal(robot_location, butter_location, goal_location, None, None, 0)
frontier.append(start)
BFS_for_robot(start)
# IDS(start)

write_on_file("result" + file_name[4] + ".txt")

if len(goal_location) == 0:
    print(path)
else:
    print("can’t pass the butter")
