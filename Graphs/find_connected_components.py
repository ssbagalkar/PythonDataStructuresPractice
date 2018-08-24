#https://www.geeksforgeeks.org/find-number-of-islands

# Input = [[1, 1, 0, 0, 0],
				 # [, 1, 0, 0, 1],
				 # [1, 0, 0, 1, 1],
				 # [0, 0, 0, 0, 0],
				 # [1, 0, 1, 0, 1]]
# Output : 5

class Graph:
	def __init__(self, row , col, graph):
		self.row = row
		self.col = col
		self.graph = graph
	
	# Function to check if a node is valid and can be processed
	# Here we check 
	# 1.if i and j are within bounds
	# 2.if the node is not visited
	# 3.if node is one(1) which indicates an island
	def is_valid(self, i, j, visited):
		return (i>=0 and i<self.row and 
						j>=0 and j<self.col and 
						not visited[i][j] and self.graph[i][j])
						
	# DFS
	def dfs(self, i, j, visited):
		row_neighbour_idx = [-1, -1, -1, 0, 0, 1, 1, 1]
		col_neighbour_idx = [-1, 0, 1, -1, 1, -1, 0, 1]
		
		visited[i][j]= True
		
		# Recur for all 8 neighbours
		for k in range(8):
			if self.is_valid(i+row_neighbour_idx[k], j+col_neighbour_idx[k], visited):
				self.dfs(i+row_neighbour_idx[k], j+col_neighbour_idx[k], visited)
				
	def bwconncomp(self):
		# Boolean array to mark visited cells
		visited = [[False for j in range(self.col)]for i in range(self.row)]
		
		count=0
		for i in range(self.row):
			for j in range(self.col):
				if not visited[i][j] and self.graph[i][j]:
					self.dfs(i, j, visited)
					count+=1
		return count
	
	
graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g= Graph(row, col, graph)
 
print ("Number of islands is: {}".format(g.bwconncomp()))