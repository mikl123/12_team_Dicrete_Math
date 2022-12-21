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
    """
    Main func
    """
    print("Our module checks graph properties.\n\
If tou want to find out what components are in your graph enter 1.\n\
If you want to find out what strongly connected components are in your graph enter 2.\n\
If you want to find out what connection points are in your graph enter 3.\n\
If you want to find out what bridges are in your graph enter 4.\n\
If you want to write graph to file from file enter 5.\n\
If you want to see what return read_csv() enter 6.")
    func_type = input(">>> ")
    if func_type == "1":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print(find_connectivity_components(read_csv(file_path,False)))
    elif func_type == "2":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print(strong_connectivity_components(read_csv(file_path,True)))
    elif func_type == "3":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print(connecting_points(read_csv(file_path,False)))
    elif func_type == "4":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print(find_bridges(read_csv(file_path,False)))
    elif func_type == "5":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print("You also need to input what type of graph you want to read\
 and write(1 - oriented 2 - not oriented)")
        type_graph = input(">>> ")
        type_graph = True if type_graph == 1 else False
        print("You also need to input write path")
        write_path = input(">>> ")
        write_csv(read_csv(file_path,type_graph),write_path,type_graph)
    elif func_type == "6":
        print("You need to input path to file where graph is.")
        file_path = input(">>> ")
        print("You also need to input what type of graph you want to read\
 and write(1 - oriented 2 - not oriented)")
        type_graph = input(">>> ")
        type_graph = True if type_graph == 1 else False
        print(read_csv(file_path,type_graph))
    else:
        print("Wrong command")

if __name__=="__main__":
    main()
    import doctest
    doctest.testmod()
