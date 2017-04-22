
FINFINITY = 5000

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





def idastar(root_node):
	#print(heuristic_misplaced(root_node))
	#print(heuristic_manhattan(root_node))
	root_node.cost = heuristic_manhattan(root_node)
	root_node.total_cost = 0
	limit = root_node.cost
	loops = 0
	node = None
	depth = 0
	while limit < FINFINITY:
		loops += 1

		break
	return


