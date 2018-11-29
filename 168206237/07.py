"""
168206237 张焜承
"""
graph = dict()
graph["yuePu"] = dict()
graph["yuePu"]["cd"] = 5
graph["yuePu"]["haiBao"] = 0

graph["cd"] = dict()
graph["cd"]["drum"] = 20
graph["cd"]["guitar"] = 15

graph["haiBao"] = dict()
graph["haiBao"]["drum"] = 35
graph["haiBao"]["guitar"] = 30

graph["guitar"] = dict()
graph["guitar"]["piano"] = 20

graph["drum"] = dict()
graph["drum"]["piano"] = 10

graph["piano"] = dict()

infinity = float("inf")
costs = dict()
costs["cd"] = 5
costs["haiBao"] = 0
costs["guitar"] = infinity
costs["drum"] = infinity
costs["piano"] = infinity

parents = dict()
parents["cd"] = "yuePu"
parents["haiBao"] = "yuePu"
parents["guitar"] = None
parents["piano"] = None
processed = []
# 以上是对整个散列表的生成


# 找到未处理节点开销最小的点
def find_lowest_cost_node(costs1):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs1:
        cost1 = costs1[node]
        if cost1 < lowest_cost and node not in processed:
            lowest_cost = cost1
            lowest_cost_node = node
    return lowest_cost_node


node1 = find_lowest_cost_node(costs)
while node1 is not None:
    cost = costs[node1]
    neighbors = graph[node1]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node1
    processed.append(node1)
    node1 = find_lowest_cost_node(costs)


# 最短路径生成 reverse函数反向
def find_short_road():
    node2 = "piano"
    short_road = ["piano"]
    while node2 != "yuePu":
        node2 = parents[node2]
        short_road.append(node2)
    short_road.reverse()
    return short_road


print(find_short_road())
