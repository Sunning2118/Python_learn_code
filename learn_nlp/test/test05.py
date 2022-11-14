# 题目一：建立一个行程数组。比如：航班如下
# Flights:
# ORD --> DNV
# SFO --> NYC
# LAX --> SFO
# NYC --> ORD

# （1） 每一个城市只到达一次，例如，从ORD出发到DNV（ORD --> DNV），不存在，从DNV返回ORD的情况。
# （2） 只存在一个行程

# Vertex使用字典connectedTo来记录与其相连的顶点，以及每一条边的权重
class Vertex:
    # 初始化id(通常是一个字符串)，以及字典connectedTo
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # addNeighbor方法天剑一个顶点到另一个顶点的连接

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # getConnections方法返回邻接表中的所有顶点，由connectedTo来表示
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getConnect(self):
        return self.connectedTo

    # 返回当前顶点到以参数传入的顶点之间的边的权重
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.verList = {}  # 顶点的字典
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex  # verlist中的元素是vertex类
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, f, t, cost=0):
        if f not in self.verList:
            nv = self.addVertex(f)
        if t not in self.verList:
            nv = self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t].getId(), cost)

    def getVertices(self):
        return self.verList.keys()

    def getnumVertices(self):
        return self.numVertices

    def __iter__(self):
        return iter(self.verList.values())


def DFS(G, start):  # start为起始点名称
    stack = []
    stack.append(start)
    seen = []
    seen.append(start)
    while stack:
        vertex = stack.pop()  # 栈，取出最后一个并删掉 先进后出
        nodesList = G.verList[vertex].getConnections()  # 找这一点的所有邻居
        for w in nodesList:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        print(vertex)


if __name__ == '__main__':
    G = Graph()
    FlightsList = ['LAX', 'SFO', 'NYC', 'ORD', 'DNV']
    for FlightName in FlightsList:
        FlightName = str(FlightName)
        G.addVertex(FlightName)
    print(G.getnumVertices())
    G.addEdge(str('LAX'), str('SFO'))
    G.addEdge(str('SFO'), str('NYC'))
    G.addEdge(str('NYC'), str('ORD'))
    G.addEdge(str('ORD'), str('DNV'))
    DFS(G, 'LAX')
