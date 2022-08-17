from stack import Stack
from queue import Queue

if __name__=='__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['F','G'],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': []
    }
    # graph above looks like:
    #         A
    #        / \
    #       B   C
    #      /     \
    #     D       E
    #    / \       \
    #   F   G       H
    # TODO: write BFS, DFS search algorithms using custom Stack and Queue classes.