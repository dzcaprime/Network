import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import game
import itertools

#数据重组，按照节点排列
def data_reorg(data):
    # 确保输入数据是一个列表的列表
    if not isinstance(data, list) or not all(isinstance(inner, list) for inner in data):
        raise ValueError("Input data must be a list of lists.")
    
    # 获取节点数量和时间序列长度
    N = len(data[0])  # 假设所有时间点的节点数量相同
    T = len(data)  # 时间序列的长度

    # 初始化新数据结构
    new_data = [[] for _ in range(N)]

    # 遍历原始数据，按照节点重新排列收益值
    for t in range(T):
        for n in range(N):
            new_data[n].append(data[t][n])

    return new_data

#计算收益差值
def calculate_changes(new_data):
    # 确保输入数据是一个列表的列表
    if not isinstance(new_data, list) or not all(isinstance(inner, list) for inner in new_data):
        raise ValueError("Input new_data must be a list of lists.")
    
    # 初始化变化值列表
    changes = []
    
    # 遍历每个节点的收益数据
    for node_data in new_data:
        # 计算变化值，即后一时刻减去当前时刻的值
        # 由于第一个时刻没有前一个时刻，所以我们从第二个时刻开始计算
        node_changes = [node_data[i + 1] - node_data[i] for i in range(len(node_data) - 1)]
        changes.append(node_changes)
    
    return changes

def calculate_all_combinations(N, t, r, p, s):
    # 预定义的收益结果
    outcomes = [t, r, p, s]

    # 使用itertools.product生成所有可能的组合
    # itertools.product接受一个可迭代对象的序列，返回所有可能的笛卡尔积
    # 这里的repeat参数N表示每个元素重复N次，即每个邻居有4种选择
    all_combinations = list(itertools.product(outcomes, repeat=N))

    # 将每个组合转换为一个元组的列表，以便于后续处理
    # 例如，如果N=2，那么一个组合可能是((t, r), (p, s))
    # 我们将其转换为[t, r, p, s]
    result = [sum(combo) for combo in all_combinations]
    unique_result = set()
    for value in result:
        unique_result.add(value)
    unique_result_list=list(unique_result)

    return unique_result_list

#find most close number in a list to a given number
def find_closest_number(num, arr):
    return min(arr, key=lambda x: abs(x - num))

def simulate(Graph, data):
    print(data)
    #去掉一个节点信息
    number_of_nodes = len(Graph.nodes())
    # 重组数据
    new_data = data_reorg(data)

    #去掉最后一个数据
    new_data=new_data[:-1]
    print(new_data)
    # 计算变化值
    changes = calculate_changes(new_data)
    print(changes)

    errors=[]
    # 计算所有可能的组合
    for i in range(number_of_nodes):
        list_neighbors=[n for n in nx.neighbors(Graph,i)]
        #print(type(list_neighbors))
        num_neighbors=len(list_neighbors)
        all_combinations = calculate_all_combinations(num_neighbors, t, r, p, s)
        #进行比较
        errori=0
        for j in range(len(changes[i])):
            #找到最接近的值
            closest=find_closest_number(changes[i][j], all_combinations)
            #计算误差
            error=abs(changes[i][j]-closest)
            errori+=error
        errors.append(errori)

    return errors

#draw the erros of the simulation
def draw_errors(errors):
    #plt.plot(errors)
    plt.scatter(hidden_graph.nodes,errors,c='blue',marker='o')
    plt.xlabel("node id")
    plt.ylabel("prediction error")
    plt.show()

t, r, p, s = 5, 3, 1, 0
test_graph=nx.Graph()
test_graph.add_nodes_from([0,1,2,3])
test_graph.add_edges_from([(0,1),(1,2),(2,0),(3,1)])
real_game=game.Game(4,test_graph,5,3,1,0)
real_game.run(10)
get_Graph = real_game.get_network()
data=real_game.get_collect()

hidden_graph=test_graph
hidden_graph.remove_node(3)

errors = simulate(hidden_graph, data)
draw_errors(errors)