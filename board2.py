import numpy as np
from hashlib import sha1

class Board2:
	def __init__(self, tiles, parent ,moves = 0):
		self.tiles = np.array(tiles, dtype=np.int8)
		"""
		print(self.tiles)
		print("")
		self.count = 0
		for row in self.tiles:
			for col in row:
				if(col == 1):
					self.count +=1
		if(self.count == 3):
			exit(0)
		"""
		#print(self.tiles)
		#print("")

		self.parent = parent

		self.cost = None # usage for idastar
		self.total_cost = None # usage for idastar 
		self.moves = moves
		self.tiles.flags.writeable = False

	def width(self):
		return self.tiles.shape[1]

	def height(self):
		return self.tiles.shape[0]

	def tilehash(self):
		return sha1(self.tiles).hexdigest()

	def is_goal(self):
		height = self.height()
		width = self.width()
		return ((self.tiles[height-1][0] == 1 and self.tiles[height-1][1] == 1) or (self.tiles[height-1][0] == 5 and self.tiles[height-1][1] == 5))

	def possible_moves(self):
		height = self.height()
		width = self.width()


		# Record Parent
		node = []
		#node.extend(self.parent)
		#node.append(self.tiles)
		#print(node)
		




		result = []
		# find empty
		goal_ys = []
		goal_xs = []
		goal_y = 0;
		goal_x = 0;
		for i in range(height):
			for j in range(width):
				if(self.tiles[i][j] == 0):
					goal_ys.append(i)
					goal_xs.append(j)
					goal_y = i
					goal_x = j
		# find the partner of zero
		s_goal_y = 0
		s_goal_x = 0
		together = False
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:# east, south, west, north
			if(goal_y + coord[0] >= 0 and goal_x + coord[1] >= 0 and goal_y+coord[0] < height and goal_x+coord[1] < width):
				if(self.tiles[goal_y+coord[0]][goal_x+coord[1]] == 0):
					s_goal_y = goal_y+coord[0]
					s_goal_x = goal_x+coord[1]
					together = True
					break

		# 1 1     3 0      4 4
		# 0 0  or 3 0  or  0 0
		if(together==True):
			if(abs(goal_y - s_goal_y) == 1):# vertical
				if(goal_x-1 >= 0):# 0 is on the east of 1
					if(self.tiles[goal_y][goal_x-1] == 3 and self.tiles[s_goal_y][s_goal_x-1]==3):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 3
						swapped_tiles[s_goal_y][s_goal_x] = 3
						swapped_tiles[goal_y][goal_x-1] = 0
						swapped_tiles[s_goal_y][s_goal_x-1] = 0
						#print('a')
						result.append(Board2(swapped_tiles, node,self.moves + 1))
				if(goal_x+1 < width):# 0 is on the west of 1
					if(self.tiles[goal_y][goal_x+1] == 3 and self.tiles[s_goal_y][s_goal_x+1]==3):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 3
						swapped_tiles[s_goal_y][s_goal_x] = 3
						swapped_tiles[goal_y][goal_x+1] = 0
						swapped_tiles[s_goal_y][s_goal_x+1] = 0
						#print('b')
						result.append(Board2(swapped_tiles, node,self.moves + 1))
			else: # horizontal
				if(goal_y-1 >= 0): # 0 is on the south of 1
					if(self.tiles[goal_y-1][goal_x] == 1 and self.tiles[s_goal_y-1][s_goal_x]==1):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 1
						swapped_tiles[s_goal_y][s_goal_x] = 1
						swapped_tiles[goal_y-1][goal_x] = 0
						swapped_tiles[s_goal_y-1][s_goal_x] = 0
						#print('c')
						result.append(Board2(swapped_tiles, node,self.moves + 1))
					if(self.tiles[goal_y-1][goal_x] == 4 and self.tiles[s_goal_y-1][s_goal_x]==4):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 4
						swapped_tiles[s_goal_y][s_goal_x] = 4
						swapped_tiles[goal_y-1][goal_x] = 0
						swapped_tiles[s_goal_y-1][s_goal_x] = 0
						#print('d')
						result.append(Board2(swapped_tiles, node,self.moves + 1))
				if(goal_y+1 < height): # 0 is on the north of 1
					if(self.tiles[goal_y+1][goal_x] == 1 and self.tiles[s_goal_y+1][s_goal_x]== 1):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 1
						swapped_tiles[s_goal_y][s_goal_x] = 1
						swapped_tiles[goal_y+1][goal_x] = 0
						swapped_tiles[s_goal_y+1][s_goal_x] = 0
						#print('e')
						result.append(Board2(swapped_tiles, node,self.moves + 1))
					if(self.tiles[goal_y+1][goal_x] == 4 and self.tiles[s_goal_y+1][s_goal_x]== 4):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[goal_y][goal_x] = 4
						swapped_tiles[s_goal_y][s_goal_x] = 4
						swapped_tiles[goal_y+1][goal_x] = 0
						swapped_tiles[s_goal_y+1][s_goal_x] = 0
						#print('f')
						result.append(Board2(swapped_tiles, node,self.moves + 1))

		# one zero
		arr = []
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:
			if(goal_y+coord[0] >= 0 and goal_x+coord[1] >= 0 and goal_y+coord[0] < height and goal_x+coord[1] < width): # check legal or not
				if(self.tiles[goal_y+coord[0]][goal_x+coord[1]] == 2):
					arr.append((goal_y+coord[0],goal_x+coord[1]))
		for coord in set(arr):
			swapped_tiles = np.copy(self.tiles)
			swapped_tiles[goal_y][goal_x] = self.tiles[coord[0]][coord[1]]
			swapped_tiles[coord[0]][coord[1]] = 0
			#print('g')
			result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 0 1 1  ==>  1 1 0
		if(goal_x + 2 < width):
			if(self.tiles[goal_y][goal_x+1] == 1 and self.tiles[goal_y][goal_x+2] == 1):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 1
				swapped_tiles[goal_y][goal_x+1] = 1
				swapped_tiles[goal_y][goal_x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(self.tiles[goal_y][goal_x+1] == 4 and self.tiles[goal_y][goal_x+2] == 4):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 4
				swapped_tiles[goal_y][goal_x+1] = 4
				swapped_tiles[goal_y][goal_x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 1 1 0  ==>  0 1 1
		if(goal_x - 2 >= 0):
			if(self.tiles[goal_y][goal_x-1] == 1  and  self.tiles[goal_y][goal_x-2] == 1):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 1
				swapped_tiles[goal_y][goal_x-1] = 1
				swapped_tiles[goal_y][goal_x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(self.tiles[goal_y][goal_x-1] == 4  and  self.tiles[goal_y][goal_x-2] == 4):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 4
				swapped_tiles[goal_y][goal_x-1] = 4
				swapped_tiles[goal_y][goal_x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# the other zero
		goal_y = goal_ys[0]
		goal_x = goal_xs[0]
		arr = []
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:
			if(goal_y+coord[0] >= 0 and goal_x+coord[1] >= 0 and goal_y+coord[0] < height and goal_x+coord[1] < width): # check legal or not
				if(self.tiles[goal_y+coord[0]][goal_x+coord[1]] == 2):
					arr.append((goal_y+coord[0],goal_x+coord[1]))
		for coord in set(arr):
			swapped_tiles = np.copy(self.tiles)
			swapped_tiles[goal_y][goal_x] = self.tiles[coord[0]][coord[1]]
			swapped_tiles[coord[0]][coord[1]] = 0
			result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 0 1 1  ==>  1 1 0
		if(goal_x + 2 < width):
			if(self.tiles[goal_y][goal_x+1] == 1 and self.tiles[goal_y][goal_x+2] == 1):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 1
				swapped_tiles[goal_y][goal_x+1] = 1
				swapped_tiles[goal_y][goal_x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(self.tiles[goal_y][goal_x+1] == 4 and self.tiles[goal_y][goal_x+2] == 4):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 4
				swapped_tiles[goal_y][goal_x+1] = 4
				swapped_tiles[goal_y][goal_x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 1 1 0  ==>  0 1 1
		if(goal_x - 2 >= 0):
			if(self.tiles[goal_y][goal_x-1] == 1  and  self.tiles[goal_y][goal_x-2] == 1):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 1
				swapped_tiles[goal_y][goal_x-1] = 1
				swapped_tiles[goal_y][goal_x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(self.tiles[goal_y][goal_x-1] == 4  and  self.tiles[goal_y][goal_x-2] == 4):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 4
				swapped_tiles[goal_y][goal_x-1] = 4
				swapped_tiles[goal_y][goal_x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		



		# *0 1 1       1 1 0
		#  0 1 1  ==>  1 1 0
		if(goal_x + 2 < width and goal_y+1 < height):
			if(self.tiles[goal_y+1][goal_x] == 0 and self.tiles[goal_y][goal_x+1] == 5 and self.tiles[goal_y][goal_x+2] == 5 and self.tiles[goal_y+1][goal_x+1] == 5 and self.tiles[goal_y+1][goal_x+2] == 5):
				#print("w")
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 5
				swapped_tiles[goal_y][goal_x+1] = 5
				swapped_tiles[goal_y][goal_x+2] = 0
				swapped_tiles[goal_y+1][goal_x] = 5
				swapped_tiles[goal_y+1][goal_x+1] = 5
				swapped_tiles[goal_y+1][goal_x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 1 1 *0  ==>  0 1 1
		# 1 1  0  ==>  0 1 1
		if(goal_x - 2 >= 0 and goal_y+1 < height):
			if(self.tiles[goal_y+1][goal_x] == 0  and  self.tiles[goal_y][goal_x-1] == 5 and self.tiles[goal_y][goal_x-2] == 5 and  self.tiles[goal_y+1][goal_x-1] == 5 and self.tiles[goal_y+1][goal_x-2] == 5):
				#print("s")
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 5
				swapped_tiles[goal_y][goal_x-1] = 5
				swapped_tiles[goal_y][goal_x-2] = 0
				swapped_tiles[goal_y+1][goal_x] = 5
				swapped_tiles[goal_y+1][goal_x-1] = 5
				swapped_tiles[goal_y+1][goal_x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# *0 0     1 1
		#  1 1     1 1
		#  1 1 ==> 0 0
		if(goal_y + 2 < height and goal_x+1 < width):
			if(self.tiles[goal_y][goal_x+1] == 0  and  self.tiles[goal_y+1][goal_x] == 5 and self.tiles[goal_y+2][goal_x] == 5 and  self.tiles[goal_y+1][goal_x+1] == 5 and self.tiles[goal_y+2][goal_x+1] == 5):
				#print("d")
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 5
				swapped_tiles[goal_y+1][goal_x] = 5
				swapped_tiles[goal_y+2][goal_x] = 0
				swapped_tiles[goal_y][goal_x+1] = 5
				swapped_tiles[goal_y+1][goal_x+1] = 5
				swapped_tiles[goal_y+2][goal_x+1] = 0
				result.append(Board2(swapped_tiles, node, self.moves + 1))
		# 1 1     0 0
		# 1 1     1 1
		#*0 0 ==> 1 1
		if(goal_y - 2 >= 0 and goal_x+1 < width):
			if(self.tiles[goal_y][goal_x+1] == 0  and  self.tiles[goal_y-1][goal_x] == 5 and self.tiles[goal_y-2][goal_x] == 5 and  self.tiles[goal_y-1][goal_x+1] == 5 and self.tiles[goal_y-2][goal_x+1] == 5):
				#print("a")
				#print("here")
				#print(self.tiles)
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[goal_y][goal_x] = 5
				swapped_tiles[goal_y-1][goal_x] = 5
				swapped_tiles[goal_y-2][goal_x] = 0
				swapped_tiles[goal_y][goal_x+1] = 5
				swapped_tiles[goal_y-1][goal_x+1] = 5
				swapped_tiles[goal_y-2][goal_x+1] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))

		return result







