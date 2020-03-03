from collections import defaultdict,deque
""" source : https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
This is BFDS for graph which is slightly different than for a tree.
"""

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def BFS(self, s):
		
		# Mark all vertices as not visited
		visited = [False] * (len(self.graph))
		
		# Create a queue for BFS
		queue = deque()
		
		# Mark the starting node as visited and enqueue items
		queue.append(s)
		visited[s-1] = True
		
		while queue:
			# deque vertex from queue and print items
			s = queue.popleft()
			print(s, end=" ")
			
			for ii in self.graph[s]:
				if visited[ii-1] == False:
					queue.append(ii)
					visited[ii-1] = True
					# Driver code


# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 1)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 1)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 4)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(6, 5)


print("Following is Breadth First Traversal"
			" (starting from vertex 0)")
g.BFS(1)



"""
Simpler implementation from https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
"""

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }
#
# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue
#
# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)
#
#   while queue:
#     s = queue.pop(0)
#     print (s, end = " ")
#
#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
#
# # Driver Code
# bfs(visited, graph, 'A')