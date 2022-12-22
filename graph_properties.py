"""
Team 12 project
"""
from typing import Dict,List
import os
import copy
from collections import defaultdict

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
                if not content[i][1] in res.keys():
                    res[content[i][1]]=[]
            else:
                other = 1 if j == 0 else 0
                res[content[i][j]].append(content[i][other])
    for key in res:
        res[key] = sorted(set(res[key]))
    return dict(res)

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
    """
    Bfs algoritm
    >>> bfs({2:[5], 3:[4, 5], 4:[3, 5], 5:[2, 3, 4]})
    [2, 5, 3, 4]
    """
    if "obhid" in kwargs and "cherga" in kwargs:
        obhid = kwargs["obhid"]
        cherga = kwargs["cherga"]
    else:
        obhid=[list(graph.keys())[0]]
        cherga=[list(graph.keys())[0]]
    for i in graph[cherga[0]]:
        if i not in obhid:
            obhid.append(i)
            cherga.append(i)
    if len(cherga) != 1:
        cherga = cherga[1:]
        bfs(graph,cherga = cherga,obhid = obhid)
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
    while len(points) > 0:
        obhid = bfs(graph,obhid = [points[0]],cherga = [points[0]])
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
    """
    Main func
    """
    print("Our module checks graph properties.\n\
If tou want to find out what components are in your graph enter 1.\n\
If you want to find out what strongly connected components are in your graph enter 2.\n\
If you want to find out what connection points are in your graph enter 3.\n\
If you want to find out what bridges are in your graph enter 4.\n\
If you want to write graph to file from file enter 5.\n\
If you want to see what return read_csv() enter 6.\n\
If you want to exit enter 7")
    while True:
        print("Lets start")
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
            type_graph = True if type_graph == "1" else False
            print("You also need to input write path")
            write_path = input(">>> ")
            write_csv(read_csv(file_path,type_graph),write_path,type_graph)
        elif func_type == "6":
            print("You need to input path to file where graph is.")
            file_path = input(">>> ")
            print("You also need to input what type of graph you want to read\
    and write(1 - oriented 2 - not oriented)")
            type_graph = input(">>> ")
            type_graph = True if type_graph == "1" else False
            print(read_csv(file_path,type_graph))
        elif func_type == "7":
            break
        else:
            print("Wrong command")
