from collections import defaultdict

'''
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number). Given some queries, return the answers.
If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

'''

C cwl
Reputation:  64
Build a graph then traversal using DFS

class Solution(object):
    def calcEquation(self, equations, values, queries):
        # Build the directicted graph with adjacency list and weight matrix.
        Adj = defaultdict(list)
        weights = {}  # Sparse matrix representation
        for (t, s), v in zip(equations, values):
            Adj[s] += t,
            Adj[t] += s,
            weights[(s, t)] = v
            weights[(t, s)] = 1. / v

        def DFS_visit(u, t, product=1., visited=set()):
            if u == t and Adj[u]:  # u in Adj is insufficient, since Adj is a defualtdict.
                return product

            visited.add(u)
            p = None
            for v in Adj[u]:
                if v not in visited:
                    p = DFS_visit(v, t, product * weights[(u, v)], visited)

                # If any search reaches t, then we are done. Otherwise, try others.
                if p:
                    break
            visited.remove(u)
            return p

        result = []
        for t, s in queries:
            result += DFS_visit(s, t) or -1,

        return result 

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"]]

print calcEquation(equations, values, queries)
