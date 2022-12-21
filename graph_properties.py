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
