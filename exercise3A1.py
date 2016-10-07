from sys import *
import traceback
from AStar2 import AStar



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
                    startPositionX = i
                    startPositionY = j
                elif inChar == 'B':
                    endPositionX = i
                    endPositionY = j
        j += 1
    ShortestPath = AStar(board, startPositionX,startPositionY,endPositionX,endPositionY)
    print ShortestPath
except:
    traceback.print_exc(file=stderr)
