"""
Team 12 project
"""
from typing import Dict,List
import os
import copy
from collections import defaultdict
import argparse

def read_csv(path:str, orientated:bool=False) -> Dict[int, List[int]]:
    pass

def write_csv(graph:dict, dst:str, orientated:bool=False)-> None:
    pass

def bfs(graph,**kwargs)->list:
    pass

def find_connectivity_components(graph:dict)->List[int]:
    pass

def connecting_points(graph:dict)->list:
    """Finds and returns all connecting_points of unoriented graph
    Args:
        graph (dict): graph(key-vertix, values-neighbour vertixes)
    Returns:
        list[int]: all connecting points
    >>> connecting_points('sadg')
    Seems it is not graph in dictionary type!
    >>> connecting_points({1:[2, 5], 2:[1, 5], 3:[4, 5], 4:[3, 5], 5:[1, 2, 3, 4]})
    [5]
    >>> connecting_points({1:[2, 3, 4], 2:[1, 3, 5],\
    3:[1, 2], 4:[1], 5:[2, 6, 8], 6:[5, 7], 7:[6, 8], 8:[5, 7]})
    [1, 2, 5]
    >>> connecting_points({1:{2, 4}, 2:{1, 3}, 3: {2, 4}, 4: {1, 3}})
    []
    """
    if not isinstance(graph, dict):
        print("Seems it is not graph in dictionary type!")
        return None
    lst = []
    for key in graph:
        new = copy.deepcopy(graph)
        new.pop(key)
        final = {}
        for i in new:
            final[i]=[k for k in new[i] if k != key]
        check = bfs(final)
        if len(check) != len(graph)-1:
            lst.append(key)
    return lst

def find_bridges(graph: dict) -> list:
    pass

def strong_connectivity_components(graph : dict, all_scc = None) ->List[int] :
    pass

def main():
    pass

if __name__=="__main__":
    main()
    import doctest
    doctest.testmod()
