# https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/
# https://gist.github.com/delijati/1629405
# https://github.com/rjoonas/AI-assignment-1
# http://stackoverflow.com/questions/33056358/python-8-puzzle-iddfs-with-results-greater-than-bfs

import numpy as np
FINFINITY = 999999

num_nodes = 0
visited = {}
flag_five = False

def heuristic_nothing(node):
	return 0

def heuristic_misplaced(node):
	#print(node.width())
	#print(node.height())
	value = int(node.tiles[node.height()-1][0] != 1) + int(node.tiles[node.height()-1][1] != 1)
	return value

def heuristic_manhattan(node):
	global flag_five
	target = 1
	if(flag_five == True):
		target = 5

	pos_y = []
	pos_x = []
	for j in range(node.height()):
		for i in range(node.width()):
			if(node.tiles[j][i] == target):
				pos_y.append(j)
				pos_x.append(i)
	goal_y = node.height()-1
	goal_x = 0
	maximum = 100
	for i in range(len(pos_y)):
		value = abs(pos_y[i] - goal_y) + abs(pos_x[i] - goal_x)
		if(value < maximum):
			maximum = value
	
	if(maximum <= 0 ):
		maximum = 1
	return maximum
	"""
	pos_y = []
	pos_x = []
	for j in range(node.height()):
		for i in range(node.width()):
			if(node.tiles[j][i] == 1):
				pos_y.append(j)
				pos_x.append(i)

	#print(pos_y)
	#print(pos_x)
	goal_y = []
	goal_y.append(node.height()-1)
	goal_y.append(node.height()-1)
	goal_x = []
	goal_x.append(0)
	goal_x.append(1)

	value = 0
	for i in range(2):
		value += abs(pos_y[i] - goal_y[i]) + abs(pos_x[i] - goal_x[i])
	return value
	"""


def search(node,threshold,depth,visited):
	#visited[node.tilehash()] = node.moves
	global num_nodes
	num_nodes+=1
	depth += 1
	#print("1")
	if(node.total_cost > threshold):
		#print("2")
		return node, node.total_cost
	if(node.is_goal()):
		#print("3")
		return node, node.total_cost
	tmp = node.possible_moves()
	minimum = FINFINITY

	"""
	new_node_list = []
	if node.moves < limit:
		for child in tmp:
			if child not in visited or visited[child.tilehash()] > child.moves:
				new_node_list.append(child)
			else:
				print("??????")
	"""


	for child in tmp:
		#print("4")
		#print(child.tiles)
		child.cost = heuristic_manhattan(child)
		#child.cost = heuristic_nothing(child)
		child.total_cost = child.cost + node.total_cost
		

		ret, newlimit = search(child,threshold,depth,visited)

		if(ret.is_goal()):
			#print("5")
			return ret, ret.total_cost
		if(newlimit < minimum):
			#print('6')
			minimum = newlimit

	return node, minimum



def search2(node,g,threshold):
	global num_nodes
	global visited
	visited[node.tilehash()] = node.moves
	num_nodes += 1
	#f = g+heuristic_misplaced(node)
	f = g+heuristic_manhattan(node)
	if(f > threshold):
		return node, f
	if(node.is_goal()):
		return node, f
	minimum = FINFINITY
	for child in node.possible_moves():
		if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
			visited[node.tilehash()] = node.moves
			#child.cost = heuristic_misplaced(child)
			child.cost = heuristic_manhattan(child)
			child.total_cost = child.cost + node.total_cost
			ret, temp = search2(child,child.total_cost,threshold)
			if(ret.is_goal()):
				return ret, ret.total_cost
			if(temp < minimum):
				minimum = temp
	return node, minimum


def idastar(root_node):
	global flag_five

	
	if(np.count_nonzero(root_node.tiles == 5) > 0):
		flag_five = True

	print("="*10+"IDASTAR"+"="*10)
	global num_nodes
	global visited
	num_nodes = 0
	#print(heuristic_misplaced(root_node))
	#print(heuristic_manhattan(root_node))
	#root_node.cost = heuristic_misplaced(root_node)
	root_node.cost = heuristic_manhattan(root_node)
	#root_node.cost = heuristic_nothing(root_node)
	root_node.total_cost = 0
	threshold = root_node.cost
	#loops = 0
	node = None
	depth = 0
	while True:
		#print(loops)
		#loops += 1
		visited = {}
		#node, tmp_limit = search(root_node,threshold,depth,visited)
		node, temp = search2(root_node,0,threshold)
		#threshold = tmp_limit + 1
		if(node.is_goal()):
			print("RESULT:")
			print(node.tiles)
			print(node.moves)
			print(num_nodes)
			break
		if(temp == FINFINITY):
			break
		threshold = temp # delete it !!!!!
	return


