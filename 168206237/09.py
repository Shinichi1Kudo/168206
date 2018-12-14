"""
168206237 张焜承
"""
graph = dict()
graph["hit"] = dict()
graph["hit"]["hot"] = 1


graph["hot"] = dict()
graph["hot"]["dot"] = 1
graph["hot"]["lot"] = 1

graph["dot"] = dict()
graph["dot"]["dog"] = 1


graph["lot"] = dict()
graph["lot"]["log"] = 1

graph["dog"] = dict()
graph["dog"]["cog"] = 1

graph["log"] = dict()
graph["log"]["cog"] = 1

graph["cog"] = dict()

infinity = float("inf")
costs = dict()
costs["hot"] = 1
costs["dot"] = infinity
costs["lot"] = infinity
costs["dog"] = infinity
costs["log"] = infinity
costs["cog"] = infinity

parents = dict()
parents["hot"] = "hit"
parents["dot"] = "hot"
parents["lot"] = "hot"
parents["log"] = "lot"
parents["dog"] = "dot"
parents["cog"] = None
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
    node2 = "cog"
    short_road = ["cog"]
    while node2 != "hit":
        node2 = parents[node2]
        short_road.append(node2)
    short_road.reverse()
    return short_road


print(find_short_road())
