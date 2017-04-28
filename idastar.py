import numpy as np
INFINITY = 999999

num_nodes = 0 # record number of nodes the algorithm traverse
visited = {}  # store the baord the algorithm has already traversed
flag_five = False # whether the 2*2 red bric exists or not
mode = 0 # 0 for heuristic manhattan, 1 for heuristic misplaced

def heuristic_misplaced(node):
	global flag_five
	target = 1
	if(flag_five == True):
		target = 5
	value = int(node.tiles[node.height()-1][0] != target) + int(node.tiles[node.height()-1][1] != target)
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
	minimum = INFINITY
	for i in range(len(pos_y)):
		value = abs(pos_y[i] - goal_y) + abs(pos_x[i] - goal_x)
		if(value < minimum):
			minimum = value
	if(minimum <= 0 ):
		minimum = 1
	return minimum

def search(node,g,threshold):
	global num_nodes
	global visited
	global mode # 0 for heuristic manhattan, 1 for heuristic misplaced
	visited[node.tilehash()] = node.moves
	num_nodes += 1
	f = 0
	if(mode == 0):
		f = g + heuristic_manhattan(node)
	else:
		f = g + heuristic_misplaced(node)
	if(f > threshold):
		return node, f
	if(node.is_goal()):
		return node, f
	minimum = INFINITY
	# collect all next possible boards
	for child in node.possible_moves():
		if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
			if(mode == 0):
				child.cost = heuristic_manhattan(child)
			else:
				child.cost = heuristic_misplaced(child)
			child.total_cost = child.cost + node.total_cost
			ret, temp = search(child,child.total_cost,threshold) # recursive call with next node as current node for depth search
			if(ret.is_goal()):
				return ret, ret.total_cost
			if(temp < minimum):
				minimum = temp
	return node, minimum


def idastar(root_node,h_mode):
	print("="*10+"IDASTAR"+"="*10)
	global flag_five
	global num_nodes
	global visited
	global mode
	if(np.count_nonzero(root_node.tiles == 5) > 0):
		flag_five = True
	num_nodes = 0
	if(h_mode == "manhattan"):
		mode = 0
		root_node.cost = heuristic_manhattan(root_node)
	else:
		mode = 1
		root_node.cost = heuristic_misplaced(root_node)
	root_node.total_cost = 0
	threshold = root_node.cost
	node = None
	while True:
		visited = {}
		node, temp = search(root_node,0,threshold)
		# whether the algorithm find the goal board or not
		if(node.is_goal()):
			print("RESULT:")
			print(node.tiles)
			print("Total Moves:")
			print(node.moves)
			print("Total Nodes IDASTAR Traverse:")
			print(num_nodes)
			if(node.parent): # show the results step by step
				print(node.parent)
			break
		if(temp >= INFINITY): # threshold larger than maximum possible f value
			print("Out of Search Space")
			break
		threshold = temp
	return


