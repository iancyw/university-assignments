from math import inf


class Graph:
    def __init__(self, gfile):
        """
        This method initialises a Graph object
        :param gfile: name of a file containing information regarding the graph
        :complexity: O(V^2)
        """
        self.graph = []
        with open(gfile) as f:                                  # opens gfile as f
            lines = f.readlines()                               # reads the lines in the file
            self.v = int(lines[0])                              # saves number of vertices equal to first line of file
            for _ in range(self.v):                             # for the number of vertices
                self.graph.append([0 for _ in range(self.v)])   # v lists with v number of elements; V^2 space, O(v^2)

            for i in range(1, len(lines)):                      # for the number of lines after 1st line in file
                line = lines[i].split()                         # split up the line from whitespace
                v1 = int(line[0])                               # first vertex
                v2 = int(line[1])                               # second vertex
                weight = int(line[2])                           # weight of the edge between v1 and v2

                self.graph[v1][v2] = weight                     # save edge into graph
                self.graph[v2][v1] = weight                     # save edge into graph for the other vertex

    def breadth_first_search(self, root):
        """
        This method does a BFS on the a node and returns the distance to the furthest nodes

        :param root: the node where the BFS will begin; the root node
        :return: the distance to the furthest nodes
        :complexity: O(V^2), as in an adjacency matrix representation, have to go along full row to find neighbours
        """
        queue = [root]                          # initialises queue for BFS
        visited = [0 for _ in range(self.v)]    # initialise visited list
        dist = [None for _ in range(self.v)]    # initialise distance list
        distance = 0                            # initialise distance
        visited[root] = 1                       # sets the root node to visited
        dist[root] = distance                   # sets the distance for root node to 0

        while queue:                            # while the queue is not empty
            current = queue.pop(0)              # pops the current node off the queue
            for i in range(len(self.graph[current])):   # checking for neighbours
                if self.graph[current][i] != 0 and visited[i] != 1:     # if its a neighbour and hasn't been visited yet
                    queue.append(i)             # append to the queue
                    dist[i] = dist[current] + 1     # distance is set
                    if dist[i] > distance:      # if current distance is larger than max distance
                        distance = dist[i]      # set current distance as max
                    visited[i] = 1              # visited is set to 1

        return distance                         # returns largest distance away from root node

    def shallowest_spanning_tree(self):
        """
        This method finds the shallowest spanning tree of the graph, which is a spanning tree which minimises the number
        of edges from the root of the spanning tree to the deepest leaf.
        :return: returns a tuple containing the vertex ID and the height of the shallowest spanning tree
        :complexity: O(V^3), run the bfs method v times.
        """
        vertex = 0                                      # vertex = current vertex with shallowest spanning tree
        shallowest = inf                                # shallowest distance
        for i in range(len(self.graph)):                # for loop continues for number of vertices in graph
            distance = self.breadth_first_search(i)     # calls bfs method; total complexity = O(v^3)
            if distance < shallowest:                   # if there is a shallower height, vertex and height is updated
                shallowest = distance
                vertex = i

        return vertex, shallowest                       # return a tuple containing the vertex id and height

    def min_index(self, distance, queue):
        """
        This method returns the index of the vertex with the minimum distance, if it is in the queue
        :param distance: list containing the distance to all vertices from a root node
        :param queue: all of the vertices in the queue
        :return: returns the vertex id that has the minimum distance
        :complexity: O(v), where v is the number of vertices in the graph.
        """
        minimum = inf                                   # initialise minimum
        min_index = 0                                   # initialise min index

        for i in range(len(distance)):                  # for number of vertices
            if distance[i] < minimum and i in queue:    # if smaller than distance and the vertex is still in queue
                minimum = distance[i]                   # set minimum distance to distance of vertex
                min_index = i                           # set minindex to vertex

        return min_index                                # the vertex with min distance

    def dijkstra(self, root):
        """
        This method uses Dijkstra's Algorithm to determine the shortest path to each vertex in the graph from a root
        :param root: the root vertex for the minimum spanning tree
        :return: returns a tuple containing the minimum distance to each vertex and their predecessors in the tree
        :complexity: O(Elog(v)); complexity for Dijkstra's algo
        """
        queue = [i for i in range(self.v)]
        distance = [inf for _ in range(self.v)]
        prev = [None for _ in range(self.v)]
        distance[root] = 0

        while queue:                                                         # while loops continues while queue = True
            current = self.min_index(distance, queue)                        # returns vertex with smallest dist; O(v)
            queue.remove(current)                                            # removes off the from pQueue; O(v)
            for i in range(len(self.graph[current])):                        # for all neighbours of current
                if self.graph[current][i] != 0:                              # checks if there is an edge connecting
                    if distance[current] + self.graph[current][i] < distance[i]:    # if dist < current saved dist
                        distance[i] = distance[current] + self.graph[current][i]    # save distance
                        prev[i] = current                                           # set predecessor to current

        return distance, prev                                                       # return distance and pred list

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
        This method finds the shortest walk which solves the constraint of picking up ice, then ice_cream and then
        getting to the destination node from a specified root node.
        :param home: the root node for the shortest walk
        :param destination: the last node for the shortest walk
        :param ice_locs: all of the locations on the graph that are valid nodes for the ice constraint
        :param ice_cream_locs: all of the locations on the graph that are valid nodes for the ice cream constraint
        :return: returns a tuple containing the length of the shortest walk found and a list containing a list of
                 vertices describing the vertices visited
        :complexity: O(Elog(v)), where E is the number of edges and v is the number of vertices in the graph.
        """
        walk = []

        ice_map = self.dijkstra(home)               # minimum spanning tree with home as the root node
        ice_min = inf
        ice_min_v = 0
        for loc in ice_locs:                        # for all locations where you can get ice
            if ice_map[0][loc] < ice_min:           # if the distance to get ice is smaller than the current min
                ice_min = ice_map[0][loc]           # set min to the distance to get to that vertex
                ice_min_v = loc                     # set the min vertex to location vertex

        ice_cream_map = self.dijkstra(ice_min_v)    # min spanning tree with the vertex where you get ice as the root
        ice_cream_min = inf
        ice_cream_min_v = 0
        for loc in ice_cream_locs:                  # for all locations where you can get ice cream
            if ice_cream_map[0][loc] < ice_cream_min:   # if the distance to get ice cream is smaller than current min
                ice_cream_min = ice_cream_map[0][loc]   # set min to the distance to get to that vertex
                ice_cream_min_v = loc                   # set the min vertex to the location vertex

        dest_map = self.dijkstra(ice_cream_min_v)       # finding the shortest path to the destination node
        dest_min = dest_map[0][destination]             # set min to the min distance need to get to destination
        dest_min_v = destination

        temp = []
        while ice_min_v is not None:                    # while the current vertex is not none
            temp.insert(0, ice_min_v)                   # insert vertex into temp (as we are going thru preds backwards)
            ice_min_v = ice_map[1][ice_min_v]           # set current vertex to predecessor
        for i in range(len(temp)):                      # for all elements in temp
            walk.append(temp[i])                        # append to walk

        # same as block above
        temp = []
        while ice_cream_min_v is not None:
            temp.insert(0, ice_cream_min_v)
            ice_cream_min_v = ice_cream_map[1][ice_cream_min_v]
        for i in range(1, len(temp)):
            walk.append(temp[i])

        # same as block above
        temp = []
        while dest_min_v is not None:
            temp.insert(0, dest_min_v)
            dest_min_v = dest_map[1][dest_min_v]
        for i in range(1, len(temp)):
            walk.append(temp[i])

        # return the distance and path of the shortest walk that satisfies all constraints
        return (ice_min + ice_cream_min + dest_min), walk
