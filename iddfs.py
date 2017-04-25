import itertools

num_nodes = 0
visited = {}

def iddfs(root_node):
	print("="*10+"FAST_IDDFS"+"="*10)
	global num_nodes
	num_nodes = 0
	#return
	for depth in itertools.count(): 
		
		queue = [root_node]
		visited = {}
		while len(queue) > 0:
			node = queue.pop() # get element from tail
			visited[node.tilehash()] = node.moves
			num_nodes+=1
			if node.is_goal():
				print("RESULT:")
				print(node.tiles)
				print("Total Moves:")
				print(node.moves)
				print("Total Nodes FAST DFS Traverse:")
				print(num_nodes)
				if(node.parent):
					print(node.parent)
				return

			if node.moves < depth:
				tmp = []
				for child in node.possible_moves():
					if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
						tmp.append(child)
				queue.extend(tmp)
		#print("="*10)

	return

def dfs(node,limit):
	global visited
	global num_nodes
	visited[node.tilehash()] = node.moves
	num_nodes += 1
	if(node.is_goal()):
		print("RESULT:")
		print(node.tiles)
		print("Total Moves:")
		print(node.moves)
		print("Total Nodes DFS Traverse:")
		print(num_nodes)
		return node

	new_node_list = []
	if node.moves < limit:
		for child in node.possible_moves():
			if child not in visited or visited[child.tilehash()] > child.moves:
				new_node_list.append(child)

	while new_node_list:
		parent = new_node_list.pop() # get element from tail
		ret = dfs(parent,limit)
		visited[node.tilehash()] = node.moves
		if ret:
			if ret.is_goal():
				return ret
	return None




def iddfs2(root_node):
	print("="*10+"IDDFS"+"="*10)
	global num_nodes
	num_nodes = 0
	for depth in itertools.count(): 
		#print(depth)
		visited = {}
		if dfs(root_node,depth):
			break
	return