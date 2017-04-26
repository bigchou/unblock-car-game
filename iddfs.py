import itertools

num_nodes = 0 # record number of nodes the algorithm traverse
visited = {}  # store the baord the algorithm has already traversed

def iddfs_queue(root_node):
	print("="*10+"IDDFS (QUEUE)"+"="*10)
	global num_nodes
	num_nodes = 0
	for depth in itertools.count():
		queue = [root_node]
		visited = {}
		# check all elements if the queue is not empty
		while len(queue) > 0:
			node = queue.pop() # get element from tail
			visited[node.tilehash()] = node.moves
			num_nodes+=1
			# whether the algorithm find the goal board or not
			if node.is_goal():
				print("RESULT:")
				print(node.tiles)
				print("Total Moves:")
				print(node.moves)
				print("Total Nodes IDDFS (QUEUE) Traverse:")
				print(num_nodes)
				if(node.parent): # show the results step by step
					print(node.parent)
				return
			# collect all next possible boards
			if node.moves < depth:
				new_node_list  = []
				for child in node.possible_moves():
					if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
						new_node_list.append(child)
				queue.extend(new_node_list)
	return

def dfs(node,depth):
	global visited
	global num_nodes
	visited[node.tilehash()] = node.moves
	num_nodes += 1
	# whether the algorithm find the goal board or not
	if(node.is_goal()):
		print("RESULT:")
		print(node.tiles)
		print("Total Moves:")
		print(node.moves)
		print("Total Nodes IDDFS (RECURSION) Traverse:")
		print(num_nodes)
		if(node.parent): # show the results step by step
			print(node.parent)
		return node
	# collect all next possible boards
	if node.moves < depth:
		for child in node.possible_moves():
			if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
				ret = dfs(child,depth) # recursive call with next node as current node for depth search
				if ret:
					if ret.is_goal():
						return ret
	return None

def iddfs_recursion(root_node):
	print("="*10+"IDDFS (RECURSION)"+"="*10)
	global num_nodes
	global visited
	num_nodes = 0
	for depth in itertools.count():
		visited = {}
		if dfs(root_node,depth):
			break
	return