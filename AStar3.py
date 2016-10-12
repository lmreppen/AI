import heapq

class node:
    def __init__(self, positionX, positionY):

def AStar(board, startX,startY, goalX,goalY):
    n0 = node(startX, startY)
    gScore = []

    openNodes = []
    closedNodes = []
    gScore.append(n0)
    calc(h(n0))
    gScore(n0) = 0
    fScore(n0) = gScore(n0) + h(n0)

    heappush(openNodes, n0)

    while openNodes is not None:
        currentNode = heappop(openNodes)
        heappush(closedNodes, currentNode)

        if(x solution):
            return x, succeeded
        neighbours = x.findNeighbours

        for n in neighbours:
            if n exists:


def attachAndEval(child, parent):
    parent(child) = parent
    gScore(child) = gScore(parent) + arcCost(parent,child)
    compute (h(child))
    fSCore(child) = gScore(child) + hScore(child)
def progogatePathImprovements(parent):
    if(gScore(parent) + arcCost(parent,child) < gScore(child):
        parent(child) = parent
        gScore(child) = gScore(parent) + arcCost(parent,child)
        fScore(child) = gScore(child) + hScore(child)

def findNeighbours(current):
    neighbours = []
        if currentNode.positionX + 1 >= 20:
            i+=1
            break
        else:
            neighbours.append(node())
            newX = currentNode.positionX + 1
            newY = currentNode.positionY
        if currentNode.positionX -1 < 0:
            i+=1
            break
        else:
            neighbours.append(node())
            newX = currentNode.positionX - 1
            newY = currentNode.positionY
        if currentNode.positionY + 1 >= 7:
            i+=1
            break
        else:
            neighbours.append(node())
            newX = currentNode.positionX
            newY = currentNode.positionY + 1
        if currentNode.positionY - 1 < 0 :
            i+=1
            break
        else:
            neighbours.append(node())
            newX = currentNode.positionX
            newY = currentNode.positionY - 1

    return neighbours
