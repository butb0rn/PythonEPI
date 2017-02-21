import unittest
class Vertex(object):
    def __init__(self,label):
        self.label = label
        self.d = -1
        self.edges = []

def isBipartite(graph):
    def hasOddCycle(v):
        q = [v]
        while q:
            prev = q.pop(0)
            for t in prev.edges:
                if t.d == -1:
                    t.d = prev.d + 1
                    q.append(t)
                elif t.d == prev.d:
                    return True
        return False

    for v in graph:
        if v.d == -1:
            v.d = 0
            if hasOddCycle(v): return False

    return True


class TestBipartite(unittest.TestCase):
    def setUp(self):
        self.g1 = Vertex("g1")
        self.g2 = Vertex("g2")
        self.g3 = Vertex("g3")
        self.g4 = Vertex("g4")
        self.g5 = Vertex("g5")
        self.g6 = Vertex("g6")
        self.g1.edges = [self.g2,self.g4,self.g5]
        self.g2.edges = [self.g1,self.g3]
        self.g3.edges = [self.g2,self.g4]
        self.g4.edges = [self.g1,self.g3,self.g6]
        self.g5.edges = [self.g1,self.g6]
        self.g6.edges = [self.g4,self.g5]
        self.GRAPH = [self.g1,self.g2,self.g3,self.g4,self.g5,self.g6]

    def test_graph_is_bipartite(self):
        self.assertEqual(isBipartite(self.GRAPH), True)

    def test_graph_is_not_bipartitle(self):
        self.g6.edges.append(self.g3) #add a wrong edge
        self.assertEqual(isBipartite(self.GRAPH), False)



if __name__ == '__main__': unittest.main()
