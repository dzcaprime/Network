import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

class Game:
    #init value
    def __init__(self,n,Graph,t,r,p,s):
        #number of nodes
        self.n = n
        #t代表背叛诱惑，r代表双方都合作，p代表双方都背叛，s代表被背叛
        #5，3，1，0
        self.t=t
        self.r=r
        self.p=p
        self.s=s
        self.G = Graph

        #0:cooperate, 1:defect
        self.strategies = [random.randint(0, 1) for i in range(n)]
        self.payoffs = [random.randint(0, 10) for i in range(n)]
        self.collect=[]
        self.update_strategies_random()
        self.update_payoffs()
        #self.update_graph()

    def update_strategies_random(self):
        for i in range(self.n):
            self.strategies[i] = random.randint(0, 1)


    def update_payoffs(self):
        for i in range(self.n):
            #节点与邻居进行博弈游戏
            neighbors=self.G.neighbors(i)
            for j in neighbors:
                if self.strategies[i] == 0 and self.strategies[j] == 0:
                    self.payoffs[i] += self.r
                elif self.strategies[i] == 0 and self.strategies[j] == 1:
                    self.payoffs[i] += self.s
                elif self.strategies[i] == 1 and self.strategies[j] == 0:
                    self.payoffs[i] += self.t
                elif self.strategies[i] == 1 and self.strategies[j] == 1:
                    self.payoffs[i] += self.p

    def update_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if self.strategies[i] == self.strategies[j]:
                        self.G[i][j]['weight'] = self.r
                    else:
                        self.G[i][j]['weight'] = self.s

    def update_strategy(self, i):
        if self.payoffs[i] < self.payoffs[i]:
            self.strategies[i] = random.randint(0, 2)

    def update(self):
        self.update_strategies_random()
        self.update_payoffs()
        #self.update_graph()

    def draw(self):
        pos = nx.spring_layout(self.G)
        labels = {}
        for i in range(self.n):
            labels[i] = self.strategies[i]
        nx.draw(self.G, pos, with_labels=True, labels=labels)
        plt.show()

    def run(self, steps):
        for i in range(steps):
            self.update()
            self.collect.append(self.payoffs.copy())
            #self.draw()
    
    def get_collect(self):
        return self.collect
    
    def get_network(self):
        return self.G

# Path: Dynamics/main.py
'''
test_graph=nx.Graph()
test_graph.add_nodes_from([0,1,2,3])
test_graph.add_edges_from([(0,1),(1,2),(2,0),(3,1)])
game=Game(4,test_graph,5,3,1,0)
game.run(10)
print(game.get_collect())
'''