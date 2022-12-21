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
    pass

def strong_connectivity_components(graph : dict, all_scc = None) ->List[int] :
    """
    This function does a forward_backward algorithm on the graph,
using bfs traversal to find all strong connectivity components.
    Args:
        graph (dict): key: vertex, values: neighbour vertixes
    Check if input data is valid. If was given not a dictionary then gives error
    "Seems like your graph is not dictionary! Write it in dict\
format(key: vertex, values: neighbour vertixes)"
    Returns:
        List[int]: min value of every scc.
    >>> strong_connectivity_components({2:[5], 3:[4], 4:[], 5: [3, 4]})
    [2, 3, 4, 5]
    >>> strong_connectivity_components({0: [1], 1: [0], 2: [3, 4], 3: [2],\
    4: [2, 5], 5: [4], 6: [10, 8], 7: [9], 8: [10,\
    9, 6], 9: [10, 8, 7], 10: [8, 9, 6]})
    [0, 2, 6]
    >>> strong_connectivity_components(3)
    'Seems like your graph is not dictionary! Write \
it in dict format(key: vertex, values: neighbour vertixes)'
    >>> strong_connectivity_components({})
    >>> strong_connectivity_components({0: [2,3], 1: [0], 2: [1], 3: [4], 4: []})
    [0, 3, 4]
    >>> strong_connectivity_components({1: {3}, 2: {1, 4}, 3: {2, 4},\
4: {5}, 5: {4}, 6: {7}, 7: {}})
    [1, 4, 6, 7]
    """
    if all_scc is None:
        all_scc = []
    if not isinstance(graph,dict) :
        return "Seems like your graph is not dictionary! Write it in dict \
format(key: vertex, values: neighbour vertixes)"
    if not graph.keys() :
        return None
    ver = [i for i in graph.keys()][0]
    front_way = set(bfs(graph, obhid = [ver], cherga=[ver]))
    new_graph = defaultdict(list)
    for vertex in graph :
        for edge in graph[vertex] :
            new_graph[edge].append(vertex)
    back_way = set(bfs(new_graph, obhid = [ver], cherga = [ver]))
    missed = set(graph.keys()).difference(back_way.union(front_way))
    scc = front_way.intersection(back_way)
    all_scc.append(min(list(scc)))
    graph1 = defaultdict(list)
    for i in front_way.difference(scc) :
        graph1[i] = copy.deepcopy(graph[i])
    strong_connectivity_components(graph1,all_scc)
    for i in missed :
        graph1[i] = copy.deepcopy(graph[i])
    strong_connectivity_components(graph1,all_scc)
    for i in back_way.difference(scc):
        graph1[i] = copy.deepcopy(graph[i])
    strong_connectivity_components(graph1, all_scc)
    return list(set(all_scc))

def main():
    pass

if __name__=="__main__":
    main()
    import doctest
    doctest.testmod()
