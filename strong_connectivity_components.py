from typing import List, Dict
from collections import defaultdict
from copy import deepcopy

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

    if len(cherga) != 1:
        cherga = cherga[1:]
        bfs(graph,cherga = cherga,obhid = obhid)
    return obhid

def forward_backward(graph : dict, all_scc = None) ->List[int] :
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
    >>> forward_backward({2:[5], 3:[4], 4:[], 5: [3, 4]})
    [2, 3, 4, 5]
    >>> forward_backward({0: [1], 1: [0], 2: [3, 4], 3: [2],\
    4: [2, 5], 5: [4], 6: [10, 8], 7: [9], 8: [10,\
    9, 6], 9: [10, 8, 7], 10: [8, 9, 6]})
    [0, 2, 6]
    >>> forward_backward(3)
    'Seems like your graph is not dictionary! Write\
    it in dict format(key: vertex, values: neighbour vertixes)'
    >>> forward_backward({})
    None
    >>> forward_backward({0: [2,3], 1: [0], 2: [1], 3: [4], 4: []})
    [0, 3, 4]
    """
    if all_scc is None:
        all_scc = []
    if not isinstance(graph,dict) :
        return "Seems like your graph is not dictionary! Write it in dict \
format(key: vertex, values: neighbour vertixes)"
    if not graph.keys() :
        return

    #1.select a pivot from graph

    ver = [i for i in graph.keys()][0]

    #2.do a bfs forward traversal

    front_way = set(bfs(graph, obhid = [ver], cherga=[ver]))
    new_graph = defaultdict(list)
    for vertex in graph :
        for edge in graph[vertex] :
            new_graph[edge].append(vertex)

    #3.do a bfs backward traversal

    back_way = set(bfs(new_graph, obhid = [ver], cherga = [ver]))
    missed = set(graph.keys()).difference(back_way.union(front_way))

    #4.find the intersection between 2 and 3, this is a scc, append
    #the minial value from this set to the list of all scc components

    scc = front_way.intersection(back_way)


    all_scc.append(min(list(scc)))
    graph1 = defaultdict(list)
    #5.form a new graph( keys and values = 2 intersection 4))
    #6.use recursion for the graph in step 5
    for i in front_way.difference(scc) :
        graph1[i] = deepcopy(graph[i])
    forward_backward(graph1,all_scc)

    #9.form a new graph( keys and values = graph intersection (3 union 4)))
    #10.use recursion for the graph in step 9

    for i in missed :
        graph1[i] = deepcopy(graph[i])
    forward_backward(graph1,all_scc)

    #9.form a new graph( keys and values = 3 intersection 4))
    #10.use recursion for the graph in step 7
    for i in back_way.difference(scc):
        graph1[i] = deepcopy(graph[i])
    forward_backward(graph1, all_scc)

    #11. return all strong connectivity components

    return list(set(all_scc))
