# UNBLOCK CAR GAME
Use IDDFS and IDASTAR to play the game

![start](https://github.com/bigchou/unblock-car-game/blob/master/start.jpg)
![goal](https://github.com/bigchou/unblock-car-game/blob/master/goal.jpg)

# Reference
  - [IDA-Star(IDA*) Algorithm in general](https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/)
  - [Sliding 8-puzzle / n-puzzle solver in Python, compares BFS, IDDFS and A*. -- rjoonas](https://github.com/rjoonas/AI-assignment-1)
  - [gistfile1.py -- delijati](https://gist.github.com/delijati/1629405)
  - [python idastar vs astar solving 8 puzzle](http://stackoverflow.com/questions/8903259/python-idastar-vs-astar-solving-8-puzzle)
  - [Python 8-puzzle IDDFS with results greater than BFS](http://stackoverflow.com/questions/33056358/python-8-puzzle-iddfs-with-results-greater-than-bfs)

 

### [QuickStart](https://github.com/bigchou/unblock-car-game/blob/master/main.py)


Example output
==============

```.
Enter the name of the test file: 
board3.txt
board is loaded!
(1) IDDFS (RECURSION)
(2) IDDFS (QUEUE)
(3) IDASTAR
Choose your input(enter -1 to exit): 
1
==========IDDFS (RECURSION)==========
RESULT:
[[2 2 2 3]
 [2 4 4 3]
 [5 5 0 2]
 [5 5 0 2]]
Total Moves:
57
Total Nodes IDDFS (RECURSION) Traverse:
312349
0:01:53.983832
(1) IDDFS (RECURSION)
(2) IDDFS (QUEUE)
(3) IDASTAR
Choose your input(enter -1 to exit): 
2
==========IDDFS (QUEUE)==========
RESULT:
[[2 2 2 3]
 [2 4 4 3]
 [5 5 0 2]
 [5 5 0 2]]
Total Moves:
57
Total Nodes IDDFS (QUEUE) Traverse:
315175
0:01:53.809987
(1) IDDFS (RECURSION)
(2) IDDFS (QUEUE)
(3) IDASTAR
Choose your input(enter -1 to exit): 
3
==========IDASTAR==========
RESULT:
[[2 2 2 3]
 [2 4 4 3]
 [5 5 0 2]
 [5 5 0 2]]
Total Moves:
57
Total Nodes IDASTAR Traverse:
414070
0:04:55.462786
(1) IDDFS (RECURSION)
(2) IDDFS (QUEUE)
(3) IDASTAR
Choose your input(enter -1 to exit): 
-1
```