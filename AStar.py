class searchNode(object):
    def __init__(self, state, positionX, positionY, f, g):
        self.state = state
        self.positionX = positionX
        self.positionY = positionY
        self.f = f
        self.g = g


def AStar(board, startX,startY, goalX, goalY):


    startNode = searchNode('start', startX, startY, 0 + calcHeuristicCost(startX, startY, goalX, goalY),0)

    closedNodes = [None]
    openNodes = [startNode]

    fScore = [[float('inf') for x in range(len(board[0]))] for y in range(len(board))]
    gScore = [[float('inf') for x in range(len(board[0]))] for y in range(len(board))]
    cameFrom = [[None for x in range(len(board[0]))] for y in range(len(board))]

    gScore[startY][startX] = 0

    fScore[startY][startX] = calcHeuristicCost(startX,startY,goalX,goalY)
    height = len(board)
    width = len(board[0])

    counter = 0
    while openNodes is not None:
        counter += 1
        openNodes = sorted(openNodes, key=lambda searchNode: searchNode.f)
        currentNode = openNodes[0]

        if currentNode.state == 'goal' or (currentNode.positionX == goalX and currentNode.positionY == goalY):
            print "Goal!"
            #return reconstruct_path(cameFrom, current)
            break

        closedNodes.append(openNodes.pop(0))

        newX = 0
        newY = 0
        for i in range (4):
            exists = False
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

            tentGScore = gScore[currentNode.positionY][currentNode.positionX] + board[newY][newX]
            print tentGScore
            for ob in openNodes:
                if(ob.positionX == newX and ob.positionY == newY):
                    exists = True
            if exists == False:
                openNodes.append(searchNode('In progress',newX ,newY , currentNode.g + calcHeuristicCost(newX, newY, goalX, goalY) + board[newY][newX],currentNode.g + board[newY][newX]))
        s    elif(tentGScore >= gScore[newY][newX]):
                i += 1
                break
            cameFrom[newY][newX] = currentNode
            gScore[newY][newX] = tentGScore
            fScore[newY][newX] = gScore[newY][newX] + calcHeuristicCost(newX, newY, goalX, goalY)
            i += 1
    #Return a list of the nodes that exist in the shortes path
    return None

def calcHeuristicCost(currentNodeX,currentNodeY,goalNodeX,goalNodeY):
    return abs(currentNodeX - goalNodeX) + abs(currentNodeY - goalNodeY)
