class GraphVertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = []


def cloneGraph(g):
    if not g: return None
    q = [g]
    dic = {g: GraphVertex(g.label)}

    while q:
        v = q.pop(0)
        for e in v.edges:
            if e not in dic.keys():
                dic[e] = GraphVertex(e.label)
                q.append(e)

            dic[v].edges.append(dic[e])

    return dic[g]
