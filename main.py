from board import Board
from board2 import Board2
from iddfs import iddfs,iddfs2
from idastar import idastar
import datetime as dt

"""
board = Board2( [[2,3,4],
				[0,0,5],
				[1,1,6]] , None)
"""


"""
board = Board2( [[2,3,4],
				[1,1,5],
				[0,0,6]])
"""



"""
board = Board2( [[2,3,4],
				[1,1,5],
				[0,6,0]], None)
"""

"""
board = Board2( [[2,3,0],
				[1,1,4],
				[0,6,5]])
"""
"""
board = Board2( [[0,2,2],
				[1,1,2],
				[0,2,2]])
"""
"""
board = Board2( [[0,2,3],
				[1,1,4],
				[0,6,5]], None)
"""

"""
board = Board2( [[0,2,2],
				[1,1,2],
				[0,2,2]])
"""

"""
board = Board( [[0,2,3],
				[1,1,4],
				[0,6,5]])
"""

"""
board = Board( [[0,2,3],
				[0,1,1],
				[4,5,6]])
"""

"""
board = Board2( [[0,2,2],
				[0,1,1],
				[2,2,2]])
"""

"""
board = Board( [[0,3,0],
				[2,1,1],
				[4,5,6]])
"""


"""
board = Board( [[2,0,0],
				[3,1,1],
				[4,5,6]])
"""


"""
board = Board2( [[6,1,1],
				[0,2,3],
				[0,4,5]])
"""

"""
board = Board2( [[2,1,1],
				[0,2,2],
				[0,2,2]],[None])
"""


"""
board = Board( [[0,2,1,1],
				[0,2,3,4],
				[7,7,5,6]])
"""

"""
board = Board( [[0,6,1,1],
				[0,6,2,3],
				[7,7,4,5]])
"""

"""
board = Board2( [[0,3,1,1],
				[0,3,2,2],
				[4,4,2,2]],[None])
"""

"""
board = Board( [[1,1,2,3],
				[1,1,9,9],
				[0,4,8,6],
				[5,0,8,7]])
"""
"""
board = Board2( [[5,5,2,2],
				[5,5,4,4],
				[0,2,3,2],
				[2,0,3,2]],[None])
"""
"""
board = Board2( [[2,2,4,4],
				[5,5,3,2],
				[5,5,3,2],
				[0,0,2,2]],[None])
"""

"""
board = Board( [[2,3,8,8],
				[1,1,0,0],
				[1,1,9,4],
				[6,7,9,5]])
"""

"""
board = Board( [[1,1,2,3],
				[1,1,8,8],
				[0,5,9,6],
				[4,0,9,7]])
"""

"""
board = Board2( [[5,5,2,2],
				[5,5,4,4],
				[2,3,0,2],
				[2,3,0,2]],[None])
"""


"""
board = Board( [[2,1,1,3],
				[0,1,1,4],
				[0,8,9,9],
				[5,8,6,7]])
"""

"""
board = Board2( [[2,5,5,2],
				[0,5,5,2],
				[0,3,4,4],
				[2,3,2,2]],[None])
"""

"""
board = Board( [[2,1,1,4],
				[3,1,1,5],
				[8,6,9,9],
				[8,0,0,7]])
"""

"""
board = Board2( [[2,5,5,2],
				[0,5,5,2],
				[0,3,4,4],
				[2,3,2,2]],[None])
"""

"""
board = Board( [[2,1,1,0],
				[3,1,1,4],
				[8,6,0,5],
				[8,7,9,9]])
"""

board = Board2( [[2,3,5,5],
				[2,3,5,5],
				[0,2,4,4],
				[2,0,2,2]],[None])


start = dt.datetime.now()
iddfs(board)
end = dt.datetime.now()
print(end-start)


"""
start = dt.datetime.now()
iddfs(board)
end = dt.datetime.now()
print(end-start)

start = dt.datetime.now()
idastar(board)
end = dt.datetime.now()
print(end-start)

start = dt.datetime.now()
iddfs2(board)
end = dt.datetime.now()
print(end-start)
"""
