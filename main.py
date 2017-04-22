from board import Board
from iddfs import iddfs,iddfs2
import datetime as dt

"""
board = Board( [[2,3,4],
				[0,0,5],
				[1,1,6]])
"""


"""
board = Board( [[2,3,4],
				[1,1,5],
				[0,0,6]])
"""


board = Board( [[0,2,3],
				[1,1,4],
				[0,6,5]])


"""
board = Board( [[0,2,3],
				[1,1,4],
				[0,6,5]])
"""


"""
board = Board( [[6,1,1],
				[0,2,3],
				[0,4,5]])
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
board = Board( [[1,1,2,3],
				[1,1,9,9],
				[0,4,8,6],
				[5,0,8,7]])
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
board = Board( [[2,1,1,3],
				[0,1,1,4],
				[0,8,9,9],
				[5,8,6,7]])
"""

"""
board = Board( [[2,1,1,4],
				[3,1,1,5],
				[8,6,9,9],
				[8,0,0,7]])
"""

"""
board = Board( [[2,1,1,0],
				[3,1,1,4],
				[8,6,0,5],
				[8,7,9,9]])
"""

start = dt.datetime.now()
iddfs2(board)
end = dt.datetime.now()
print(end-start)
