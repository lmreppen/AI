from sys import *
import traceback
#from AStar2 import AStar
from  AStar4 import pathFind



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
                #board[j][i] = float('inf')
                board[j][i] = '#'
            else:
                board[j][i] = '.';
                if inChar == 'A':
                    startPositionX = i
                    startPositionY = j
                    board[j][i] = 'A'
                elif inChar == 'B':
                    endPositionX = i
                    endPositionY = j
                    board[j][i] = 'B'
        j += 1

    dirs = 4 # number of possible directions to move on the map
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    #ShortestPath = AStar(board, startPositionX,startPositionY,endPositionX,endPositionY)
    ShortestPath = pathFind(board,20,7,dirs,dx,dy,startPositionX,startPositionY,endPositionX,endPositionY)
    print ShortestPath
except:
    traceback.print_exc(file=stderr)
