import networkx as nx
import random
import numpy as np
from matplotlib import pyplot as plt

def small_world (N,k,p):
    Matrix=np.zeros((N,N))
    for i in range(N):
        t=0
        #生成k规则网络，节点的度为k
        while(t<k/2):
            Matrix[i][i-(t+1)]=1
            Matrix[i-(t+1)][i]=1
            t+=1
    for i in range(N):
        t=0
        while(t<N/2):
            if(Matrix[i][i-(t+1)]==1):
                if random.random()<p:
                    #进行随机加边
                    targetNode=random.randint(0,(N-1))
                    while(targetNode==i)or Matrix[i][targetNode]==1:
                        #如果已经存在这条边或者是本身，重新生成
                        targetNode=random.randint(0,(N-1))
                    Matrix[i][targetNode]=1
                    Matrix[targetNode][i]=1
            t+=1
    return Matrix

def plt_graph(Matrix,axis=None):
    g=nx.from_numpy_array(Matrix)
    pos=nx.circular_layout(g)
    nodeSize=[]
    maxSize=100
    minSize=10
    maxDegree=np.max(np.sum(Matrix,axis=0))
    minDegree=np.min(np.sum(Matrix,axis=0))
    if maxDegree==minDegree:
        nodeSize=[maxSize for i in range(len(Matrix))]
    else:
        for node in g:
            size=((np.sum(Matrix[node]))-minDegree)/(maxDegree-minDegree)*(maxSize-minSize)+minSize
            nodeSize.append(size)
    
    nx.draw_networkx_nodes(g,pos=pos,node_color='blue',node_size=nodeSize,alpha=0.6,ax=axis)
    nx.draw_networkx_edges(g,pos=pos,width=0.3,alpha=0.6,ax=axis)
    print('最短路径距离',nx.average_shortest_path_length(g))
    print('平均聚类系数',nx.average_clustering(g))
    print('边数',nx.number_of_edges(g))
#给定网络生成参数，N：节点数，k：节点的度，p：重连概率
N=30
k=4
p=0.1

G=small_world(N,k,p)
#两个图，一行两列
fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(6,3))
ax[0].matshow(G,cmap='gray')
plt_graph(G,axis=ax[1])
plt.title('NW small world')
plt.show()
