import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def calcHeuristicCost(currentNodeX,currentNodeY,goalNodeX,goalNodeY):
    return abs(currentNodeX - goalNodeX) + abs(currentNodeY - goalNodeY)

def findNeighbours(board, current):
    newX = 0
    newY = 0
    for i in range (4):
        if i == 0:
            if currentNode.positionX + 1 >= width:
                i+=1
                break
            else:
                newX = currentNode.positionX + 1
                newY = currentNode.positionY
        elif i == 1:
            if currentNode.positionX -1 < 0:
                i+=1
                break
            else:
                newX = currentNode.positionX - 1
                newY = currentNode.positionY
        elif i == 2:
            if currentNode.positionY + 1 >= height:
                i+=1
                break
            else:
                newX = currentNode.positionX
                newY = currentNode.positionY + 1
        elif i == 3:
            if currentNode.positionY - 1 < 0 :
                i+=1
                break
            else:
                newX = currentNode.positionX
                newY = currentNode.positionY - 1
        for ob in closedNodes:
            if(ob != None):
                if(ob.positionX == newX and ob.positionY == newY):
                    i+=1

def AStar(board, startX,startY, goalX, goalY):
