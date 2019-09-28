class Node:
    '''Node class'''

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(field, start, end):

    '''
    Main A* implementation by Avocado2000 (16)
    :param field: The maze as a multidimensional array
    :param start: Start node as Node() object
    :param end:   End node as Node() object
    :return: Backtrace path of nodes to the goal node
    '''

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node   = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    print(f"START: {start_node.position}")
    print(f"END:   {end_node.position}")

    openList   = []
    closedList = []

    openList.append(start_node)

    while len(openList) > 0:

        currentNode = openList[0]
        cur_index = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                cur_index = index

        openList.pop(cur_index)
        closedList.append(currentNode)

        if currentNode == end_node:
            # Backtrace path
            path = []
            current = currentNode
            while current.parent:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []

        # Adjacent squares
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_pos = (currentNode.position[0] + new_pos[0], currentNode.position[1] + new_pos[1])
            for num, pos in enumerate(node_pos):
                print(f"{num}: {pos}")

            # In Range
            if node_pos[0] > (len(field) - 1) or node_pos[0] < 0 or node_pos[1] > (len(field[len(field)-1]) -1) or node_pos[1] < 0:
                continue

            # Walkable (everything else than 0, when 0, empty and not walkable)
            if field[node_pos[0]][node_pos[1]] != 0:
                print(f"Walkable: {field[node_pos[0]][node_pos[1]]}")
                continue

            new_node = Node(currentNode, node_pos)
            print(f"NEW NODE: {new_node.position}")

            children.append(new_node)

        for child in children:
            print(f"CHILD POSITION: {child.position}")

            for closed_child in closedList:
                if child == closed_child:
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for oNode in openList:
                if child == oNode and child.g > oNode.g:
                    continue

            openList.append(child)

def main():

    maze = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end   = (3, 4)

    result = astar(maze, start, end)
    print("RES:", result)

main()
