import unittest
class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.status = 0
        #0 -> clear | 1 -> processing | 2 -> done

def findCycle(g):
    if not g: return False

    for v in g.edges:
        if v.status == 0 and hasCycle(v): return True

    return False

def hasCycle(g):
    if g.status == 1: return True
    g.status = 1

    for v in g.edges:
        if v.status != 2:
            if hasCycle(v): return True
    g.status = 2
    return False


class TestFindCycleMethod(unittest.TestCase):
    def test_no_cycle_with_none_graph(self):
        p1 = None
        self.assertEqual(findCycle(p1), False)

    def test_no_cycle_with_one_vertex(self):
        p1 = Vertex("p1")
        self.assertEqual(findCycle(p1), False)

    def test_no_cycle_with_three_vertex(self):
        p1,p2,p3 = Vertex("p1"), Vertex("p2"), Vertex("p3")
        p1.edges.append(p2)
        p2.edges.append(p3)
        self.assertEqual(findCycle(p1), False)

    def test_has_cycle_with_three_vertex(self):
        p1,p2,p3 = Vertex("p1"), Vertex("p2"), Vertex("p3")
        p1.edges.append(p2)
        p2.edges.append(p3)
        p3.edges.append(p2)
        self.assertEqual(findCycle(p1), True)



if __name__ == '__main__': unittest.main()
