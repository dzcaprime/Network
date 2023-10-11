import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

#generate a ER random network
def ER(N,p):
    Matrix=np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            if random.random()<p:
                Matrix[i][j]=1
                Matrix[j][i]=1
    return Matrix


