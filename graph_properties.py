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
    """
    Bfs algoritm
    >>> bfs({2:[5], 3:[4, 5], 4:[3, 5], 5:[2, 3, 4]})
    [2, 5, 3, 4]
    """
    if "obhid" in kwargs and "cherga" in kwargs:
        obhid=kwargs["obhid"]
        cherga=kwargs["cherga"]
    else:
        obhid=[list(graph.keys())[0]]
        cherga=[list(graph.keys())[0]]
    for i in graph[cherga[0]]:
        if i not in obhid:
            obhid.append(i)
            cherga.append(i)
    if len(cherga)!=1:
        cherga=cherga[1:]
        bfs(graph,cherga=cherga,obhid=obhid)
    return obhid

def find_connectivity_components(graph:dict)->List[int]:
    pass

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
