import sys
from board2 import Board2
from iddfs import iddfs_recursion,iddfs_queue
from idastar import idastar
import datetime as dt


def Readfile(filename):
	inputboard = []
	with open(filename) as f:
		for row in f:
			row = [ int(x) for x in row.split()]
			inputboard.append(row)
	return inputboard

def ShowBoard(inputboard):
	for row in inputboard:
		for col in row:
			sys.stdout.write(str(col)+' ')
			sys.stdout.flush()
		sys.stdout.write('\n')



# READFILE
print("Enter the name of the test file: ")
filename = str(sys.stdin.readline())
filename = filename.rstrip('\n')
inputboard = Readfile(filename)
print("Board is loaded!")

# MENU
while(True):
	print('Current Board: ')
	ShowBoard(inputboard)
	board = Board2(inputboard,[None])
	print("(1) IDDFS (RECURSION)")
	print("(2) IDDFS (QUEUE)")
	print("(3) IDASTAR (heuristic manhattan)")
	print("(4) IDASTAR (heuristic misplaced)")
	print("Choose your input(enter -1 to exit): ")
	option = int(sys.stdin.readline())
	if(option == -1):
		exit(0)
	elif(option == 1):
		start = dt.datetime.now()
		iddfs_recursion(board)
		end = dt.datetime.now()
		print(end-start)
	elif(option == 2):
		start = dt.datetime.now()
		iddfs_queue(board)
		end = dt.datetime.now()
		print(end-start)
	elif(option == 3):
		start = dt.datetime.now()
		idastar(board,'manhattan')
		end = dt.datetime.now()
		print(end-start)
	elif(option == 4):
		start = dt.datetime.now()
		idastar(board,'misplaced')
		end = dt.datetime.now()
		print(end-start)
	else:
		print("Invalid Input, Try Again... ")
	print("\n\n")