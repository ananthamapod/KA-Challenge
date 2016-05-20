from models.graph import Graph
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

if __name__ == "__main__":
    names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
    ids = list(range(1,20))
    g = Graph()
    for i in range(len(names)):
        g.add_user(names[i], ids[i], i)

    choice = int(raw_input("Input test case number: "))
    if choice == 1:
        g.connect("a","b")
        g.connect("b","d")
        #total_infection(g, "b")
        pdb.set_trace()
        limited_infection(g, "b", 5)
    elif choice == 2:
        g.connect("a","b")
        #total_infection(g, "g")
        pdb.set_trace()
        limited_infection(g, "g", 5)
    else:
        g.connect("a","b")
        g.connect("b","d")
        g.connect("d","h")
        g.connect("d","i")
        g.connect("d","j")
        g.connect("c","h")
        g.connect("c","g")
        g.connect("e","h")
        g.connect("e","g")
        g.connect("e","f")
        g.connect("h","k")
        g.connect("h","l")
        g.connect("h","m")
        g.connect("h","n")
        g.connect("k","o")
        g.connect("l","p")
        g.connect("n","q")
        g.connect("n","r")
        g.connect("o","s")
        #total_infection(g, "d")
        pdb.set_trace()
        limited_infection(g, "h", 10)

    for k,v in g.v.items(): print k + ":" + str(v.version)
