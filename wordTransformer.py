import threading
import copy

__completedPaths = []
def __BFS_Parallel(paths, visited, queue, goal):
    if len(queue) == 0:
        return
    path = queue.pop(0)
    node = path[-1]
    if node not in visited:
        neighbors = paths[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                possible_path = list(path)
                possible_path.append(neighbor)
                queue.append(possible_path)
                if neighbor == goal:
                    __completedPaths.append(possible_path)
                    return
    visited.append(node)
    if len(queue) > 1:
        half = len(queue)//2
        q1 = queue[:half]
        q2 = queue[half:]
        t1 = threading.Thread(target=__BFS_Parallel, args=(paths, copy.deepcopy(visited), q1, goal))
        t2 = threading.Thread(target=__BFS_Parallel, args=(paths, copy.deepcopy(visited), q2, goal))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    elif len(queue) > 0:
        __BFS_Parallel(paths, visited, queue, goal)
    return

def __BFS_Iterative(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                possible_path = list(path)
                possible_path.append(neighbor)
                queue.append(possible_path)
                if neighbor == goal:
                    return possible_path
            visited.append(node)
    print(f"No viable paths from {start} to {goal}")
    return None

def __clean_dictionary(dictionary, start, goal):
    if len(start) != 5:
        print(f"ERROR: start ({start}) is not five characters!")
        return None
    if len(goal) != 5:
        print(f"ERROR: goal ({goal}) is not five characters!")
        return None

    dictionary.append(start)
    dictionary.append(goal)
    #Remove Duplicates
    dictionary = list(set(dictionary))

    #Remove any words of not length five
    ret = []
    for val in dictionary:
        if len(val) == 5:
            ret.append(val.lower())
        else:
            print(f"WARNING: {val} was removed because it is not of length 5")
    return ret

def __find_connections(dictionary):
    links = {}
    for val in dictionary:
        sublinks = []
        for others in dictionary:
            if others == val:
                continue
            differences = 0
            for x in range(0,5):
                if val[x] != others[x]:
                    differences += 1
                if differences > 1:
                    break
            if differences == 1:
                sublinks.append(others)
        links[val] = sublinks
    return links

def BFS_Iterative(dictionary, start, goal):
    start = start.lower()
    goal = goal.lower()

    if start == goal:
        print(f"Iterative: The shortest Path is {[start,goal]}")
        return [start, goal]

    dictionary = __clean_dictionary(dictionary, start, goal)
    if dictionary is None:
        return None
    connections = __find_connections(dictionary)
    shortestPath = __BFS_Iterative(connections, start, goal)
    print(f"Iterative: The shortest Path is {shortestPath}")
    return shortestPath

def BFS_Parallel(dictionary, start, goal):
    start = start.lower()
    goal = goal.lower()

    if start == goal:
        print(f"Parallel: The shortest Path is {[start,goal]}")
        return [start, goal]

    global __completedPaths
    __completedPaths = []

    dictionary = __clean_dictionary(dictionary, start, goal)
    if dictionary is None:
        return None
    connections = __find_connections(dictionary)

    __BFS_Parallel(connections, [], [[start]], goal)
    #print(f'Completed Paths are {__completedPaths}')
    
    if len(__completedPaths) == 0:
        print(f"No path between {start} and {goal} found!")
        return None
    shortestPath = min(__completedPaths, key=len)
    print(f"Parallel: The shortest Path is {shortestPath}")
    return shortestPath

dictionary = ['start', 'stark', 'stack', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
start = 'smart'
goal = 'brain'
BFS_Iterative(dictionary, start, goal)
BFS_Parallel(dictionary, start, goal)

    