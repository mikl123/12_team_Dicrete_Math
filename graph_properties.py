"""
Team 12 project
"""
from typing import Dict,List
import os
import copy
from collections import defaultdict
import argparse

def read_csv(path:str, orientated:bool=False) -> Dict[int, List[int]]:
    """
    Reads graph from csv-file and returns this graph in dictionary-format.
    Args:
        path (str): path to a csv-file you want to read
        orientated (bool): True if graph orientated, False if not orientated
    Returns:
        dict: keys - verteces of the graph, values- related vertices
    >>> read_csv(12, True)
    Write a path(str) to the csv-file
    >>> read_csv('58123618294', False)
    No file was found
    """
    if not isinstance(path, str):
        print("Write a path(str) to the csv-file")
        return None
    if not os.path.exists(path):
        print("No file was found")
        return None
    if os.path.isdir(path):
        print("You need to input file not directory")
        return None
    if not path.split(".")[-1]=="csv":
        print("You need to .csv file")
        return None
    res=defaultdict(lambda: [])
    with open(path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    content = [list(map(int, i.strip().split(','))) for i in content]
    for i in range(len(content)):
        for j in range(2):
            if orientated:
                res[content[i][0]].append(content[i][1])
            else:
                other = 1 if j == 0 else 0
                res[content[i][j]].append(content[i][other])
    for key in res:
        res[key] = sorted(set(res[key]))
    return dict(res)

def write_csv(graph:dict, dst:str, orientated:bool=False)-> None:
    pass

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
