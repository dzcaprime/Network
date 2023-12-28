import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#CI,DC,BC,CC,EC,NC
#k-core
#input: graph G
#output: the k-core value of each node as a dictionary
def k_core(G):
    k_core = {}
    k = 1
    min_degree_nodes=[]
    while nx.number_of_nodes(G) > 0:
        curr_min_degree_nodes = [node for node, degree in G.degree() if degree < k]
        min_degree_nodes+=curr_min_degree_nodes
        while(len(curr_min_degree_nodes)>0):
            G.remove_nodes_from(curr_min_degree_nodes)
            curr_min_degree_nodes=[node for node,degree in G.degree() if degree<k]
            min_degree_nodes+=curr_min_degree_nodes
        
        for node in min_degree_nodes:
            k_core[node] = k-1

        min_degree_nodes.clear()
        
        k += 1
    
    return k_core
