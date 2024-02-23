import itertools

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

# 示例：计算当邻居数量N为2时的所有可能组合
N = 3
t, r, p, s = 5, 3, 1, 0
all_possible_outcomes = calculate_all_combinations(N, t, r, p, s)

# 打印结果
print("All possible outcomes:", all_possible_outcomes)