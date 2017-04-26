import numpy as np
from hashlib import sha1

show_step_or_not = False # show the results step by step if you set this option true

class Board2:
	def __init__(self, tiles, parent ,moves = 0):
		self.tiles = np.array(tiles, dtype=np.int8)
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
		#==========================
		# Record Parent
		node = []
		if(show_step_or_not):
			node.extend(self.parent)
			node.append(self.tiles)
		#==========================
		result = [] # Record all possible boards
		# find all blank tiles
		blk_coord_ys = []
		blk_coord_xs = []
		for i in range(height):
			for j in range(width):
				if(self.tiles[i][j] == 0):
					blk_coord_ys.append(i)
					blk_coord_xs.append(j)
		y = blk_coord_ys[1]
		x = blk_coord_xs[1]
		# check the blank_tile_1 is near the blank_tile_2
		ex_y = 0
		ex_x = 0
		together = False
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:# east, south, west, north
			if(y + coord[0] >= 0 and x + coord[1] >= 0 and y+coord[0] < height and x+coord[1] < width):
				if(self.tiles[y+coord[0]][x+coord[1]] == 0):
					ex_y = y+coord[0]
					ex_x = x+coord[1]
					together = True
					break
		# 1 1    3 0    4 4
		# 0 0 or 3 0 or 0 0 ... etc.
		if(together==True):
			if(abs(y - ex_y) == 1):# blank_tile_1 and blank_tile_2 are perpendicular to each other
				# 3 0    0 3
				# 3 0 => 0 3
				if(x-1 >= 0):
					if(self.tiles[y][x-1] == 3 and self.tiles[ex_y][ex_x-1]==3):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 3
						swapped_tiles[ex_y][ex_x] = 3
						swapped_tiles[y][x-1] = 0
						swapped_tiles[ex_y][ex_x-1] = 0
						result.append(Board2(swapped_tiles, node,self.moves + 1))
				# 0 3    3 0
				# 0 3 => 3 0
				if(x+1 < width):
					if(self.tiles[y][x+1] == 3 and self.tiles[ex_y][ex_x+1]==3):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 3
						swapped_tiles[ex_y][ex_x] = 3
						swapped_tiles[y][x+1] = 0
						swapped_tiles[ex_y][ex_x+1] = 0
						result.append(Board2(swapped_tiles, node,self.moves + 1))
			else: # blank_tile_1 and blank_tile_2 are parallel to each other
				if(y-1 >= 0):
					# 1 1    0 0
					# 0 0 => 1 1
					if(self.tiles[y-1][x] == 1 and self.tiles[ex_y-1][ex_x]==1):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 1
						swapped_tiles[ex_y][ex_x] = 1
						swapped_tiles[y-1][x] = 0
						swapped_tiles[ex_y-1][ex_x] = 0
						result.append(Board2(swapped_tiles, node,self.moves + 1))
					# 4 4    4 4
					# 0 0 => 0 0
					if(self.tiles[y-1][x] == 4 and self.tiles[ex_y-1][ex_x]==4):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 4
						swapped_tiles[ex_y][ex_x] = 4
						swapped_tiles[y-1][x] = 0
						swapped_tiles[ex_y-1][ex_x] = 0
						result.append(Board2(swapped_tiles, node,self.moves + 1))
				if(y+1 < height):
					# 0 0    1 1
					# 1 1 => 0 0
					if(self.tiles[y+1][x] == 1 and self.tiles[ex_y+1][ex_x]== 1):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 1
						swapped_tiles[ex_y][ex_x] = 1
						swapped_tiles[y+1][x] = 0
						swapped_tiles[ex_y+1][ex_x] = 0
						result.append(Board2(swapped_tiles, node,self.moves + 1))
					# 0 0    4 4
					# 4 4 => 0 0
					if(self.tiles[y+1][x] == 4 and self.tiles[ex_y+1][ex_x]== 4):
						swapped_tiles = np.copy(self.tiles)
						swapped_tiles[y][x] = 4
						swapped_tiles[ex_y][ex_x] = 4
						swapped_tiles[y+1][x] = 0
						swapped_tiles[ex_y+1][ex_x] = 0
						#print('f')
						result.append(Board2(swapped_tiles, node,self.moves + 1))

		
		for i in range(2):
			if(i > 0):
				y = blk_coord_ys[0]
				x = blk_coord_xs[0]
			# Consider the tile(type 2) is the neighbor of the blank tiles
			arr = []
			for coord in [(0,1),(1,0),(0,-1),(-1,0)]:
				if(y+coord[0] >= 0 and x+coord[1] >= 0 and y+coord[0] < height and x+coord[1] < width): # check legal or not
					if(self.tiles[y+coord[0]][x+coord[1]] == 2):
						arr.append((y+coord[0],x+coord[1]))
			for coord in set(arr):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[y][x] = self.tiles[coord[0]][coord[1]]
				swapped_tiles[coord[0]][coord[1]] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
			

			if(x + 2 < width):
				# 0 1 1 => 1 1 0
				if(self.tiles[y][x+1] == 1 and self.tiles[y][x+2] == 1):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 1
					swapped_tiles[y][x+1] = 1
					swapped_tiles[y][x+2] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))
				# 0 4 4 => 4 4 0
				if(self.tiles[y][x+1] == 4 and self.tiles[y][x+2] == 4):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 4
					swapped_tiles[y][x+1] = 4
					swapped_tiles[y][x+2] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(x - 2 >= 0):
				# 1 1 0 => 0 1 1
				if(self.tiles[y][x-1] == 1  and  self.tiles[y][x-2] == 1):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 1
					swapped_tiles[y][x-1] = 1
					swapped_tiles[y][x-2] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))
				# 4 4 0 => 0 4 4
				if(self.tiles[y][x-1] == 4  and  self.tiles[y][x-2] == 4):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 4
					swapped_tiles[y][x-1] = 4
					swapped_tiles[y][x-2] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(y + 2 < height):
				# 0    3
				# 3    3
				# 3 => 0
				if(self.tiles[y+1][x] == 3  and  self.tiles[y+2][x] == 3):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 3
					swapped_tiles[y+1][x] = 3
					swapped_tiles[y+2][x] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))
			if(y - 2 >= 0):
				# 3    0
				# 3    3
				# 0 => 3
				if(self.tiles[y-1][x] == 3  and  self.tiles[y-2][x] == 3):
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[y][x] = 3
					swapped_tiles[y-1][x] = 3
					swapped_tiles[y-2][x] = 0
					result.append(Board2(swapped_tiles, node,self.moves + 1))

		# *0 1 1       1 1 0
		#  0 1 1  ==>  1 1 0
		if(x + 2 < width and y+1 < height):
			if(self.tiles[y+1][x] == 0 and self.tiles[y][x+1] == 5 and self.tiles[y][x+2] == 5 and self.tiles[y+1][x+1] == 5 and self.tiles[y+1][x+2] == 5):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[y][x] = 5
				swapped_tiles[y][x+1] = 5
				swapped_tiles[y][x+2] = 0
				swapped_tiles[y+1][x] = 5
				swapped_tiles[y+1][x+1] = 5
				swapped_tiles[y+1][x+2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# 1 1 *0  ==>  0 1 1
		# 1 1  0  ==>  0 1 1
		if(x - 2 >= 0 and y+1 < height):
			if(self.tiles[y+1][x] == 0  and  self.tiles[y][x-1] == 5 and self.tiles[y][x-2] == 5 and  self.tiles[y+1][x-1] == 5 and self.tiles[y+1][x-2] == 5):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[y][x] = 5
				swapped_tiles[y][x-1] = 5
				swapped_tiles[y][x-2] = 0
				swapped_tiles[y+1][x] = 5
				swapped_tiles[y+1][x-1] = 5
				swapped_tiles[y+1][x-2] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		# *0 0     1 1
		#  1 1     1 1
		#  1 1 ==> 0 0
		if(y + 2 < height and x+1 < width):
			if(self.tiles[y][x+1] == 0  and  self.tiles[y+1][x] == 5 and self.tiles[y+2][x] == 5 and  self.tiles[y+1][x+1] == 5 and self.tiles[y+2][x+1] == 5):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[y][x] = 5
				swapped_tiles[y+1][x] = 5
				swapped_tiles[y+2][x] = 0
				swapped_tiles[y][x+1] = 5
				swapped_tiles[y+1][x+1] = 5
				swapped_tiles[y+2][x+1] = 0
				result.append(Board2(swapped_tiles, node, self.moves + 1))
		# 1 1     0 0
		# 1 1     1 1
		#*0 0 ==> 1 1
		if(y - 2 >= 0 and x+1 < width):
			if(self.tiles[y][x+1] == 0  and  self.tiles[y-1][x] == 5 and self.tiles[y-2][x] == 5 and  self.tiles[y-1][x+1] == 5 and self.tiles[y-2][x+1] == 5):
				swapped_tiles = np.copy(self.tiles)
				swapped_tiles[y][x] = 5
				swapped_tiles[y-1][x] = 5
				swapped_tiles[y-2][x] = 0
				swapped_tiles[y][x+1] = 5
				swapped_tiles[y-1][x+1] = 5
				swapped_tiles[y-2][x+1] = 0
				result.append(Board2(swapped_tiles, node,self.moves + 1))
		return result







