from sys import *
import traceback
from AStar import AStar
from AStar import calcHeuristicCost



def printBoard(board):
    for x in board:
        print x
        print '\n'

#Leser inn filen og lager en matrise av brettet.
#Finner startposisjon og sluttposisjon.
try:
    startPosition = []
    endPosition = []
    n = stdin
    board = [[0 for x in range(20)] for y in range(7)]
    j = 0
    for line in n:
        for i in range(20):
            inChar = line[i]
            if inChar == '#':
                board[j][i] = float('inf')
            else:
                board[j][i] = 1;
                if inChar == 'A':
                    startPosition.append(i)
                    startPosition.append(j)
                elif inChar == 'B':
                    endPosition.append(i)
                    endPosition.append(j)

        j += 1
    ShortestPath = AStar(board, startPosition, endPosition)
    print ShortestPath
except:
    traceback.print_exc(file=stderr)
