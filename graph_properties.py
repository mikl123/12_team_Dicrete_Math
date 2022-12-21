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
    pass

def find_bridges(graph: dict) -> list:
    """
    We have to find all bridges in an unoriented graph
    The idea: to run dfs on the original graph
    To cut off edges iteratively and run bfs on the modified graph
    Compare bfs len results
    If different - treat edge as a bridge
    Finds bridges of graph
    Args:
        graph (dict): graph(key-vertix, values-neighbour vertixes)
    Returns:
        list[int]: all connecting points
    >>> find_bridges({1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3, 5], 5:[4, 6, 8],\
 6:[5, 7], 7:[6, 8], 8:[5, 7]})
    [(4, 5)]
    >>> find_bridges({1: [2], 2:[1, 3, 6], 3:[2, 4, 18], 4:[3, 5], 5:[4],\
 6:[2, 7, 8], 7:[6, 9], 8:[9, 6], 9:[7, 8, 10], 10:[9, 11, 14, 15], \
11:[10, 12], 12:[11, 13], 13:[12, 14], 14:[10, 13], 15:[10, 16, 18], \
16:[15, 17], 17:[18, 16], 18:[3, 15, 17]})
    [(1, 2), (3, 4), (4, 5)]
    >>> find_bridges({1:[2, 3], 2:[1, 3], 3:[1, 2]})
    []
    """
    if not isinstance(graph, dict):
        print("Seems it is not graph in dictionary type!")
        return None
    lst = []
    count_components = len(find_connectivity_components(graph))
    all_checks=[]
    for key in graph:
        for elem in graph[key]:
            if (elem,key) not in all_checks:
                all_checks.append((key,elem))
    for rebro in all_checks:
        buf= copy.deepcopy(graph)
        buf[rebro[0]].remove(rebro[1])
        buf[rebro[1]].remove(rebro[0])
        count_components_check = len(find_connectivity_components(buf))
        if count_components_check > count_components:
            lst.append(tuple(sorted(rebro)))
    return lst

def strong_connectivity_components(graph : dict, all_scc = None) ->List[int] :
    pass

def main():
    pass

if __name__=="__main__":
    main()
    import doctest
    doctest.testmod()
