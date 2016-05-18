from models.graph import Graph
import collections

"""Total infection algorithm, uses breadth first expansion to infect
at each vertex"""
def total_infection(kaGraph, username):
    # Aliasing for convenience
    v = kaGraph.v
    e = kaGraph.e

    # Check for user's existence
    if not v.get(username):
        print "Invalid username"
        return None

    # Modified BFS
    visited = {username}
    Q = collections.deque()
    startNode = v[username]
    version = startNode.version
    Q.append(startNode)
    while len(Q) > 0:
        curr = Q.popleft()
        curr.version = version
        nodes = list(e[curr.name].students)
        nodes.extend(e[curr.name].teachers)
        for r in nodes:
            if r not in visited:
                Q.append(v[r])
        visited.add(curr.name)

"""Limited infection algorithm, uses breadth first expansion to infect
at each vertex"""
def limited_infection(kaGraph, username, n):
    pass

if __name__ == "__main__":
    names = ["a", "b", "c", "d"]
    ids = [1, 2, 3, 4]
    g = Graph()
    for i in range(len(names)):
        g.add_user(names[i], ids[i], i)

    import pdb; pdb.set_trace()
    g.connect("b","a")
    g.connect("c", "a")
    g.connect("d", "a")
    total_infection(g, "d")
