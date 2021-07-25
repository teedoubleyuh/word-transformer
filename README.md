# Brief
This repo contains the python solution to an arbitrary coding problem as stated below.

# Problem Statement
Given two five letter words, A and B, and a dictionary of five letter words, find a shortest transformation from A to B, such that only one letter can be changed at a time and all intermediate words in the transformation must exist in the dictionary. For example, if A and B are "smart" and "brain", the result may be:
smart
 start
 stack
 slack
 black
 blank
 bland
 brand
 braid
brain

# Solution
We can start by going through the dictionary one by one and finding all the corresponding values in the dictionary that have just one letter different, in order to start planning a path. Once this is done, it becomes apparent that this is an unweighted graph traversal problem, or it can be thought of as a weighted graph traversal where all paths have a cost of 1. A vanilla Breadth First Search algorithm is selected as it is well suited to finding the shortest path in an unweighted graph, whereas Depth First Search and Djikstra's algorithm are better suited to finding shortest path in a weighted graph.

## Iterative Approach
An iterative implementation of the BFS alogorithm is provided for single threaded operation. It takes the dictionary, the start word, and the goal word as inputs and returns the shortest path as a list, if no path is found it returns None.

## Recursive Multithreaded Approach
A recursive implementation of the BFS alogorithm is provided for multi threaded operation. It takes the dictionary, the start word, and the goal word as inputs and returns the shortest path as a list, if no path is found it returns None. The multithreaded approach naively splits the queue containing possible paths in half when there is more than one half continues the recursion of each half in a thread, if there is only one possible path, the recursion continues single threaded.

# Running
A simple driver example is provided in the module. Running yields the following results:
```
python3 wordTransformer.py
Iterative: The shortest Path is ['smart', 'start', 'stark', 'stack', 'slack', 'black', 'blank', 'bland', 'brand', 'braid', 'brain']
Parallel: The shortest Path is ['smart', 'start', 'stark', 'stack', 'slack', 'black', 'blank', 'bland', 'brand', 'braid', 'brain']
```
# Testing
A set of tests are provided for the two approaches. Since the two approaches provide the same output with the same inputs pytest test parameterization is employed where the parameratized value is the function call, so each test will run once calling BFS_Iterative and once running BFS_Parallel.

Use the following command to run test cases from the root directory of the repository:
```
python3 -m pytest
```