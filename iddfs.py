import itertools

num_nodes = 0
visited = {}

def iddfs(root_node):
	print("="*10+"IDDFS (QUEUE)"+"="*10)
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
				print("Total Nodes IDDFS (QUEUE) Traverse:")
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
	#print(node.tiles)
	visited[node.tilehash()] = node.moves
	num_nodes += 1
	if(node.is_goal()):
		print("RESULT:")
		print(node.tiles)
		print("Total Moves:")
		print(node.moves)
		print("Total Nodes IDDFS (RECURSION) Traverse:")
		print(num_nodes)
		return node

	new_node_list = []
	if node.moves < limit:
		
		for child in node.possible_moves():

			#if(child.tilehash() in visited):
				#print(visited)

			if child.tilehash() not in visited or visited[child.tilehash()] > child.moves:
				"""
				if child not in visited:
					print("T")

				try: 
					print(visited[child.tilehash()])
				except:
					print("err")
				"""
				new_node_list.append(child)
	


	while new_node_list:
		parent = new_node_list.pop(0) # get element from tail
		ret = dfs(parent,limit)
		#visited[node.tilehash()] = node.moves
		if ret:
			#visited[node.tilehash()] = node.moves
			if ret.is_goal():
				return ret
	return None




def iddfs2(root_node):
	print("="*10+"IDDFS (RECURSION)"+"="*10)
	global num_nodes
	global visited
	num_nodes = 0
	for depth in itertools.count(): 
		#print(depth)
		visited = {}
		if dfs(root_node,depth):
			break
		#print("="*10)
	return