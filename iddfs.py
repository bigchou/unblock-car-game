import itertools

def iddfs(root_node):
	print("="*10+"IDDFS"+"="*10)
	#return
	for depth in itertools.count(): 
		queue = [root_node]
		visited = {}
		while len(queue) > 0:
			node = queue.pop()
			visited[node.tilehash()] = node.moves
			if node.is_goal():
				print("RESULT:")
				print(node.tiles)
				print(node.moves)
				return
			if node.moves < depth:
				tmp = []
				for child in node.possible_moves():
					if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
						tmp.append(child)
				queue.extend(tmp)
		#print("="*10)

	return

def dfs(node,deep,limit,visited):
	if(node.is_goal()):
		print("RESULT:")
		print(node.tiles)
		print(node.moves)
		return node

	tmp = node.possible_moves()
	new_node_list = []
	for i in tmp:
		if i not in visited:
			visited.append(i)
			obj_node = i
			new_node_list.append(obj_node)

	while new_node_list and deep < limit:
		parent = new_node_list.pop(0)
		ret = dfs(parent,deep+1,limit,visited)
		if ret:
			if ret.is_goal():
				return ret
	return None

def iddfs2(root_node):
	limit = 0
	ret = None
	while True:
		print(limit)
		visited = []
		ret = dfs(root_node,0,limit,visited)
		limit += 1
		if ret:
			break
	return ret