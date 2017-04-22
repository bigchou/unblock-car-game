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