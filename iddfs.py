import itertools

num_nodes = 0


def iddfs(root_node):
	print("="*10+"IDDFS"+"="*10)
	global num_nodes
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
				print(node.moves)
				print(num_nodes)
				return

			if node.moves < depth:
				tmp = []
				for child in node.possible_moves():
					if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
						tmp.append(child)
				queue.extend(tmp)
		#print("="*10)

	return

def dfs(node,limit,visited):
	visited[node.tilehash()] = node.moves
	global num_nodes
	num_nodes += 1
	if(node.is_goal()):
		print("RESULT:")
		print(node.tiles)
		print(node.moves)
		print(num_nodes)
		return node

	new_node_list = []
	if node.moves < limit:
		for child in node.possible_moves():
			if child not in visited or visited[child.tilehash()] > child.moves:
				new_node_list.append(child)


	while new_node_list:
		parent = new_node_list.pop() # get element from tail
		ret = dfs(parent,limit,visited)
		if ret:
			if ret.is_goal():
				return ret
	return None




def iddfs2(root_node):
	for depth in itertools.count(): 
		#print(depth)
		visited = {}
		if dfs(root_node,depth,visited):
			break
	return