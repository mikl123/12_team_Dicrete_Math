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
    """Reads dictionary graph and writes it in csv-file.
    Args:
        graph (dict): key: vertex, values: neighbour vertixes
        dst (str): name of file you want to write your file to
        orientated (bool): checking whether graph orientated or no
    Returns: Nothing
    >>> write_csv('sdg', 'new_test_notorientated.csv', False)
    Seems like your graph is not dictionary!\
Write it in dict format(key: vertex, values: neighbour vertixes)
    >>> write_csv({1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3, 5],\
 5:[4, 6, 8], 6:[5, 7], 7:[6, 8], 8:[5, 7]}, 'test1', True)
    """
    if not isinstance(graph, dict):
        print("Seems like your graph is not dictionary!\
Write it in dict format(key: vertex, values: neighbour vertixes)")
        return None
    if not isinstance(dst, str):
        print("Write a path(str) to the csv-file")
        return None
    if os.path.isdir(dst):
        print("You need to input file not directory")
        return None
    res=""
    for key in graph:
        for i in graph[key]:
            if orientated:
                res += str(key) + ',' + str(i) + '\n'
            elif f"{key},{i}" not in res and f"{i},{key}" not in res:
                res += str(key) + ',' + str(i) + '\n'
    with open(dst, 'w', encoding= 'utf-8') as file:
        file.write(res)

def bfs(graph,**kwargs)->list:
    pass

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
