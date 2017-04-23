
FINFINITY = 5000

num_nodes = 0

def heuristic_nothing(node):
	return 0

def heuristic_misplaced(node):
	#print(node.width())
	#print(node.height())
	value = int(node.tiles[node.height()-1][0] != 1) + int(node.tiles[node.height()-1][1] != 1)
	return value

def heuristic_manhattan(node):
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


def dfs_heuristic_rec(node,limit,depth):
	global num_nodes
	num_nodes+=1
	depth += 1
	#print("1")
	if(node.total_cost > limit):
		#print("2")
		return node, node.total_cost
	if(node.is_goal()):
		#print("3")
		return node, node.total_cost
	tmp = node.possible_moves()
	minimum = FINFINITY
	for child in tmp:
		#print("4")
		#print(child.tiles)
		child.cost = heuristic_manhattan(child)
		#child.cost = heuristic_nothing(child)
		child.total_cost = child.cost + node.total_cost
		

		ret, newlimit = dfs_heuristic_rec(child,limit,depth)

		if(ret.is_goal()):
			#print("5")
			return ret, ret.total_cost
		if(newlimit < minimum):
			#print('6')
			minimum = newlimit

	return node, minimum




def idastar(root_node):
	#print(heuristic_misplaced(root_node))
	#print(heuristic_manhattan(root_node))
	root_node.cost = heuristic_manhattan(root_node)
	#root_node.cost = heuristic_nothing(root_node)
	root_node.total_cost = 0
	limit = root_node.cost
	loops = 0
	node = None
	depth = 0
	while limit < FINFINITY:
		loops += 1
		node, tmp_limit = dfs_heuristic_rec(root_node,limit,depth)
		limit = tmp_limit + 1
		if(node.is_goal()):
			print("RESULT:")
			print(node.tiles)
			print(node.moves)
			print(num_nodes)
			break
	return


