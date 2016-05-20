from models.graph import Graph
from vis import Infection_Visual
import collections
import pdb

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
    # Aliasing for convenience
    v = kaGraph.v
    e = kaGraph.e

    # Check for user's existence
    if not v.get(username):
        print "Invalid username"
        return None

    # Initial stores
    # scounts - counts of number of students that need to be infectedfor each user
    scounts = {name: len(relation.students)+1 for name, relation in e.items()}
    # infection cases and infected set
    infected = {name:{'students':False, 'teachers':False} for name in v}
    is_infected = set()
    # fringe queue
    Q = collections.deque()
    startNode = v[username]
    version = startNode.version
    Q.append((username, False))

    """Internal utility function for grouping the tasks associated with infection"""
    def infect(username):
        if username not in is_infected:
            v[username].version = version
            is_infected.add(username)
            scounts[username] -= 1
            # Decrement overall counts for users to whom curr is a student
            for t in e[username].teachers:
                scounts[t] -= 1
            return True
        return False

    while len(Q) > 0 and n > 0:
        currTuple = Q.popleft()
        curr = currTuple[0]

        # Infect user if not yet infected
        if infect(curr): n -= 1

        # Is one of the parents who should have their children filled all the way
        # Refers to nodes up the tree from the starting infection node
        if currTuple[1]:
            for i in e[curr].students:
                if i not in is_infected:
                    Q.append((i, False))
                    if infect(i): n -= 1
            infected[curr]["students"] = True

        # Check the teachers
        if not infected[curr]["teachers"]:
            # Temp list of teachers who have not been infected and spread to classroom yet
            teachers = [(t, True) for t in e[curr].teachers if scounts[t] > 0 and (t, True) not in Q]

            if not infected[curr]["students"]:
                #Add current user in role of teacher to teachers list
                teachers.append((curr, True))
            # Put it all onto the queue
            Q.extend(teachers)
            infected[curr]["teachers"] = True

        # Check the students
        # Relevant to nodes down the tree from an encountered node
        # Includes starting node
        elif not infected[curr]["students"]:
            for i in e[curr].students:
                if i not in is_infected:
                    Q.append((i, False))
                    if infect(i): n -= 1
            infected[curr]["students"] = True

        # Resort priorities in queue
        Q = collections.deque(sorted(Q, key=lambda x: scounts[x[0]]))

"""            teachers = collections.deque(sorted(teachers, key=lambda x: scounts[x]))
            while len(teachers) > 0:
                t = teachers.popleft()
                tNode = v[t]
                tEdges = e[t]
                if scounts[t] < n:
                    # note, if already infected, does nothing
                    infect(tNode)
                    for s in tEdges.students:
                        # likewise, here. If already infected, does nothing
                        infect(v[s])
                    teachers = collections.deque(sorted(teachers, key=lambda x: scounts[x]))
"""


"""Simple utility to consolidate actions associated with adding an edge to the KA user graph"""
def add_edge(graph, visual, edge_start, edge_end):
    graph.connect(edge_start, edge_end)
    visual.graph.add_edge(edge_start, edge_end)

if __name__ == "__main__":
    names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
    ids = list(range(1,20))
    g = Graph()
    visual = Infection_Visual()

    for i in range(len(names)):
        g.add_user(names[i], ids[i], i)
        visual.graph.add_node(names[i])

    choice = int(raw_input("Input test case number: "))
    if choice == 1:
        add_edge(g, visual, "a","b")
        add_edge(g, visual, "b","d")
        visual.draw()
        #total_infection(g, "b")
        pdb.set_trace()
        limited_infection(g, "b", 5)
    elif choice == 2:
        add_edge(g, visual, "a","b")
        visual.draw()
        #total_infection(g, "g")
        pdb.set_trace()
        limited_infection(g, "g", 5)
    else:
        add_edge(g, visual, "a","b")
        add_edge(g, visual, "b","d")
        add_edge(g, visual, "d","h")
        add_edge(g, visual, "d","i")
        add_edge(g, visual, "d","j")
        add_edge(g, visual, "c","h")
        add_edge(g, visual, "c","g")
        add_edge(g, visual, "e","h")
        add_edge(g, visual, "e","g")
        add_edge(g, visual, "e","f")
        add_edge(g, visual, "h","k")
        add_edge(g, visual, "h","l")
        add_edge(g, visual, "h","m")
        add_edge(g, visual, "h","n")
        add_edge(g, visual, "k","o")
        add_edge(g, visual, "l","p")
        add_edge(g, visual, "n","q")
        add_edge(g, visual, "n","r")
        add_edge(g, visual, "o","s")
        visual.draw()
        #total_infection(g, "d")
        pdb.set_trace()
        limited_infection(g, "h", 10)

    for k,v in g.v.items(): print k + ":" + str(v.version)
