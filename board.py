


import numpy as np
from hashlib import sha1

class Board:
	def __init__(self, tiles, moves = 0):
		self.tiles = np.array(tiles, dtype=np.int8)
		#print(self.tiles)
		#print("")
		self.moves = moves
		self.tiles.flags.writeable = False


	def getFrequency(self):
		dict = {}
		one = []
		for row in self.tiles:
			for col in row:
				if(col == 0):
					continue
				if(col not in dict):
					dict[col] = 1
				else:
					dict[col] += 1	
		return dict


	def width(self):
		return self.tiles.shape[1]

	def height(self):
		return self.tiles.shape[0]

	def tilehash(self):
		return sha1(self.tiles).hexdigest()

	def is_goal(self):
		height = self.height()
		width = self.width()
		return (self.tiles[height-1][0] == 1 and self.tiles[height-1][1] == 1)

	
	def possible_moves(self):
		height = self.height()
		width = self.width()
		freq_table = self.getFrequency()
		#check_4_bric = False
		#if(freq_table[1]==4):
		#	check_4_bric = True
		#	freq_table.pop(1)
			#print(freq_table)


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
					#print('ooxx')
					break

		# === new coord after moving ===
		
		if(together==True):# two zeros (together)
			#print("here")

			for index in freq_table:
				if(freq_table[index] > 1):
					if(abs(goal_y - s_goal_y) == 1):# vertical
						#print("Here")
						if(goal_x-1 >= 0):# 0 is on the east of 1
							if(self.tiles[goal_y][goal_x-1]==index and self.tiles[s_goal_y][s_goal_x-1]==index):
								if(freq_table[1] == 4 and index == 1):
									continue
								#print("y")
								swapped_tiles = np.copy(self.tiles)
								swapped_tiles[goal_y][goal_x] = index
								swapped_tiles[s_goal_y][s_goal_x] = index
								swapped_tiles[goal_y][goal_x-1] = 0
								swapped_tiles[s_goal_y][s_goal_x-1] = 0
								result.append(Board(swapped_tiles, self.moves + 1))
						if(goal_x+1 < width):# 0 is on the west of 1
							if(self.tiles[goal_y][goal_x+1]==index and self.tiles[s_goal_y][s_goal_x+1]==index):
								if(freq_table[1] == 4 and index == 1):
									continue
								#print("o")
								swapped_tiles = np.copy(self.tiles)
								swapped_tiles[goal_y][goal_x] = index
								swapped_tiles[s_goal_y][s_goal_x] = index
								swapped_tiles[goal_y][goal_x+1] = 0
								swapped_tiles[s_goal_y][s_goal_x+1] = 0
								result.append(Board(swapped_tiles, self.moves + 1))
					else: #horizontal
						#print("here")
						if(goal_y-1 >= 0): # 0 is on the south of 1
							if(self.tiles[goal_y-1][goal_x]==index and self.tiles[s_goal_y-1][s_goal_x]==index):
								if(freq_table[1] == 4 and index == 1):
									continue
								#print("l")
								swapped_tiles = np.copy(self.tiles)
								swapped_tiles[goal_y][goal_x] = index
								swapped_tiles[s_goal_y][s_goal_x] = index
								swapped_tiles[goal_y-1][goal_x] = 0
								swapped_tiles[s_goal_y-1][s_goal_x] = 0
								result.append(Board(swapped_tiles, self.moves + 1))
						if(goal_y+1 < height): # 0 is on the north of 1
							if(self.tiles[goal_y+1][goal_x]==index and self.tiles[s_goal_y+1][s_goal_x]==index):
								if(freq_table[1] == 4 and index == 1):
									continue
								#print("k")
								swapped_tiles = np.copy(self.tiles)
								swapped_tiles[goal_y][goal_x] = index
								swapped_tiles[s_goal_y][s_goal_x] = index
								swapped_tiles[goal_y+1][goal_x] = 0
								swapped_tiles[s_goal_y+1][s_goal_x] = 0
								result.append(Board(swapped_tiles, self.moves + 1))






		# one zero

		# consider only its neighbor, and think that his neighborhood contains only one bric
		two_index = []
		for i in freq_table:
			if(freq_table[i] > 1):
				two_index.append(i)

		arr = []
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:
			if(goal_y+coord[0] >= 0 and goal_x+coord[1] >= 0 and goal_y+coord[0] < height and goal_x+coord[1] < width): # check legal or not
				if(self.tiles[goal_y+coord[0]][goal_x+coord[1]] not in two_index ):
					arr.append((goal_y+coord[0],goal_x+coord[1]))

		for coord in set(arr):
			#print('here')
			#print("ooxx")
			swapped_tiles = np.copy(self.tiles)
			swapped_tiles[goal_y][goal_x] = self.tiles[coord[0]][coord[1]]
			swapped_tiles[coord[0]][coord[1]] = 0
			result.append(Board(swapped_tiles, self.moves + 1))


		
		for index in two_index:
			
			# 0 1 1  ==>  1 1 0
			if(goal_x + 2 < width):
				if(self.tiles[goal_y][goal_x+1] == index  and  self.tiles[goal_y][goal_x+2] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					#print("here")
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y][goal_x+1] = index
					swapped_tiles[goal_y][goal_x+2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1 1 0  ==>  0 1 1
			if(goal_x - 2 >= 0):
				if(self.tiles[goal_y][goal_x-1] == index  and  self.tiles[goal_y][goal_x-2] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					#print('here')
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y][goal_x-1] = index
					swapped_tiles[goal_y][goal_x-2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))

			# 0      1
			# 1      1
			# 1  ==> 0
			if(goal_y + 2 < height):
				if(self.tiles[goal_y+1][goal_x] == index  and  self.tiles[goal_y+2][goal_x] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y+1][goal_x] = index
					swapped_tiles[goal_y+2][goal_x] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1      0
			# 1      1
			# 0  ==> 1
			if(goal_y - 2 >= 0):
				if(self.tiles[goal_y-1][goal_x] == index  and  self.tiles[goal_y-2][goal_x] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y-1][goal_x] = index
					swapped_tiles[goal_y-2][goal_x] = 0
					result.append(Board(swapped_tiles, self.moves + 1))








		# the other zero
		goal_y = goal_ys[0]
		goal_x = goal_xs[0]
		arr = []
		for coord in [(0,1),(1,0),(0,-1),(-1,0)]:
			#print("here")
			if(goal_y+coord[0] >= 0 and goal_x+coord[1] >= 0 and goal_y+coord[0] < height and goal_x+coord[1] < width): # check legal or not
				if(self.tiles[goal_y+coord[0]][goal_x+coord[1]] not in two_index):
					arr.append((goal_y+coord[0],goal_x+coord[1]))

		for coord in set(arr):
			#print("here")
			#print("ooxx")
			swapped_tiles = np.copy(self.tiles)
			swapped_tiles[goal_y][goal_x] = self.tiles[coord[0]][coord[1]]
			swapped_tiles[coord[0]][coord[1]] = 0
			result.append(Board(swapped_tiles, self.moves + 1))

		
		for index in two_index:
			
			# 0 1 1  ==>  1 1 0
			if(goal_x + 2 < width):
				if(self.tiles[goal_y][goal_x+1] == index  and  self.tiles[goal_y][goal_x+2] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					#print("here")
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y][goal_x+1] = index
					swapped_tiles[goal_y][goal_x+2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1 1 0  ==>  0 1 1
			if(goal_x - 2 >= 0):
				if(self.tiles[goal_y][goal_x-1] == index  and  self.tiles[goal_y][goal_x-2] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					swapped_tiles = np.copy(self.tiles)
					#print("here")
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y][goal_x-1] = index
					swapped_tiles[goal_y][goal_x-2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 0      1
			# 1      1
			# 1  ==> 0
			if(goal_y + 2 < height):
				if(self.tiles[goal_y+1][goal_x] == index  and  self.tiles[goal_y+2][goal_x] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y+1][goal_x] = index
					swapped_tiles[goal_y+2][goal_x] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1      0
			# 1      1
			# 0  ==> 1
			if(goal_y - 2 >= 0):
				if(self.tiles[goal_y-1][goal_x] == index  and  self.tiles[goal_y-2][goal_x] == index):
					if(freq_table[1] == 4 and index == 1):
						continue
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = index
					swapped_tiles[goal_y-1][goal_x] = index
					swapped_tiles[goal_y-2][goal_x] = 0
					result.append(Board(swapped_tiles, self.moves + 1))








		# handling 4 bric
		if(freq_table[1] == 4):
			# *0 1 1       1 1 0
			#  0 1 1  ==>  1 1 0
			if(goal_x + 2 < width and goal_y+1 < height):
				if(self.tiles[goal_y+1][goal_x] == 0 and self.tiles[goal_y][goal_x+1] == 1 and self.tiles[goal_y][goal_x+2] == 1 and self.tiles[goal_y+1][goal_x+1] == 1 and self.tiles[goal_y+1][goal_x+2] == 1):
					#print("w")
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = 1
					swapped_tiles[goal_y][goal_x+1] = 1
					swapped_tiles[goal_y][goal_x+2] = 0
					swapped_tiles[goal_y+1][goal_x] = 1
					swapped_tiles[goal_y+1][goal_x+1] = 1
					swapped_tiles[goal_y+1][goal_x+2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1 1 *0  ==>  0 1 1
			# 1 1  0  ==>  0 1 1
			if(goal_x - 2 >= 0 and goal_y+1 < height):
				if(self.tiles[goal_y+1][goal_x] == 0  and  self.tiles[goal_y][goal_x-1] == 1 and self.tiles[goal_y][goal_x-2] == 1 and  self.tiles[goal_y+1][goal_x-1] == 1 and self.tiles[goal_y+1][goal_x-2] == 1):
					#print("s")
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = 1
					swapped_tiles[goal_y][goal_x-1] = 1
					swapped_tiles[goal_y][goal_x-2] = 0
					swapped_tiles[goal_y+1][goal_x] = 1
					swapped_tiles[goal_y+1][goal_x-1] = 1
					swapped_tiles[goal_y+1][goal_x-2] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# *0 0     1 1
			#  1 1     1 1
			#  1 1 ==> 0 0
			if(goal_y + 2 < height and goal_x+1 < width):
				if(self.tiles[goal_y][goal_x+1] == 0  and  self.tiles[goal_y+1][goal_x] == 1 and self.tiles[goal_y+2][goal_x] == 1 and  self.tiles[goal_y+1][goal_x+1] == 1 and self.tiles[goal_y+2][goal_x+1] == 1):
					#print("d")
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = 1
					swapped_tiles[goal_y+1][goal_x] = 1
					swapped_tiles[goal_y+2][goal_x] = 0
					swapped_tiles[goal_y][goal_x+1] = 1
					swapped_tiles[goal_y+1][goal_x+1] = 1
					swapped_tiles[goal_y+2][goal_x+1] = 0
					result.append(Board(swapped_tiles, self.moves + 1))
			# 1 1     0 0
			# 1 1     1 1
			#*0 0 ==> 1 1
			if(goal_y - 2 >= 0 and goal_x+1 < width):
				if(self.tiles[goal_y][goal_x+1] == 0  and  self.tiles[goal_y-1][goal_x] == 1 and self.tiles[goal_y-2][goal_x] == 1 and  self.tiles[goal_y-1][goal_x+1] == 1 and self.tiles[goal_y-2][goal_x+1] == 1):
					#print("a")
					#print("here")
					#print(self.tiles)
					swapped_tiles = np.copy(self.tiles)
					swapped_tiles[goal_y][goal_x] = 1
					swapped_tiles[goal_y-1][goal_x] = 1
					swapped_tiles[goal_y-2][goal_x] = 0
					swapped_tiles[goal_y][goal_x+1] = 1
					swapped_tiles[goal_y-1][goal_x+1] = 1
					swapped_tiles[goal_y-2][goal_x+1] = 0
					result.append(Board(swapped_tiles, self.moves + 1))

		return result

