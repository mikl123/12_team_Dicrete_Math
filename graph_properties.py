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
    """
    Finds connectivity components.
    Args:
        graph (dict): key: vertex, values: neighbour vertixes
    Check if input data is valid. If was give not dictionary then gives error
    "Seems like your graph is not dictionary! Write it in dict \
format(key: vertex, values: neighbour vertixes)"
    Returns:
        List[int]: min values of every component.
    >>> find_connectivity_components({0: [1], 1: [0], 2: [3, 4], 3: [2],\
 4: [2, 5], 5: [4], 6: [10, 8], 7: [9], 8: [10,\
9, 6], 9: [10, 8, 7], 10: [8, 9, 6]})
    [0, 2, 6]
    >>> find_connectivity_components({1:[2], 2:[1], 3:[4], 4:[3]})
    [1, 3]
    >>> find_connectivity_components(123)
    'Seems like your graph is not dictionary! Write it in dict \
format(key: vertex, values: neighbour vertixes)'
    """
    if not isinstance(graph,dict):
        return "Seems like your graph is not dictionary! Write it in dict \
format(key: vertex, values: neighbour vertixes)"
    res=[]
    points=[point for point in graph]
    while len(points)>0:
        obhid=bfs(graph,obhid=[points[0]],cherga=[points[0]])
        res.append(min(obhid))
        points=[i for i in points if i not in obhid]
    return res

def connecting_points(graph:dict)->list:
    pass

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
