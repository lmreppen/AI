class searchNode(object):
    def __init__(self, state, positionX, positionY, f, g):
        self.state = state
        self.positionX = positionX
        self.positionY = positionY
        self.f = f
        self.g = g


def AStar(board, start, goal):
    startNode = searchNode('start', start[0], start[1], 0 + calcHeuristicCost(start[0], start[1], goal[0], goal[1]),0)

    closedNodes = [None]
    openNodes = [startNode]

    gScore = [[None for x in range(len(board[0]))] for y in range(len(board))]
    fScore = [[None for x in range(len(board[0]))] for y in range(len(board))]
    cameFrom = [[None for x in range(len(board[0]))] for y in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            gScore[i][j] = float('Inf')
            fScore[i][j] = float('Inf')
            cameFrom[i][j] = None
    gScore[start[0]][start[1]] = 0
    fScore[start[0]][start[1]] = calcHeuristicCost(start[0],start[1],goal[0],goal[1])

    height = len(board)
    width = len(board[0])

    while openNodes is not None:
        openNodes = sorted(openNodes, key=lambda searchNode: searchNode.f)
        currentNode = openNodes[0]

        if currentNode.state == 'goal':
            return reconstruct_path(cameFrom, current)

        closedNodes.append(openNodes.pop(0))

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
            for ob in openNodes:
                if(ob.positionX == newX and ob.positionY == newY):
                    i+=1
                    break
            for ob in closedNodes:
                if(ob != None):
                    if(ob.positionX == newX and ob.positionY == newY):
                        i+=1
                        break
            openNodes.append(searchNode('In progress',newX ,newY , currentNode.g + calcHeuristicCost(newX, newY, goal[0], goal[1]) + 1,currentNode.g + 1))
            print len(openNodes)
            print len(closedNodes)
            print '\n'

                # for ob in openNodes:
                #     if(ob.positionX == currentNode.positionX + 1 and ob.positionY == currentNode.positionY):
                #         i+=1
                #         break
                # for ob in closedNodes:
                #     if(ob != None):
                #         if(ob.positionX == currentNode.positionX + 1 and ob.positionY == currentNode.positionY):
                #             i+=1
                #             break
                # openNodes.append(searchNode('In progress',currentNode.positionX + 1 ,currentNode.positionY , currentNode.g + calcHeuristicCost(start[0], start[1], goal[0], goal[1]),1))
                    ##positionX = n. + 1
    #Return a list of the nodes that exist in the shortes path
    return None

def calcHeuristicCost(currentNodeX,currentNodeY,goalNodeX,goalNodeY):
    return abs(currentNodeX - goalNodeX) + abs(currentNodeY - goalNodeY)


#
# class searchNode(object):
#     def __init__(self, state, positionX, positionY, f, ):
#         self.state = state
#         self.positionX = positionX
#         self.positionY = positionY
#         self.f = f
#
#
# def AStar(board, start, goal):
#     startNode = searchNode('start', start[0], start[1], 0 + calcHeuristicCost(start[0], start[1], goal[0], goal[1]))
#
#     closedNodes = [None]
#     openNodes = [startNode]
#
#     gScore = [[None for x in range(len(board[0]))] for y in range(len(board))]
#     fScore = [[None for x in range(len(board[0]))] for y in range(len(board))]
#     cameFrom = [[None for x in range(len(board[0]))] for y in range(len(board))]
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             gScore[i][j] = float('Inf')
#             fScore[i][j] = float('Inf')
#             cameFrom[i][j] = None
#     gScore[start[0]][start[1]] = 0
#     fScore[start[0]][start[1]] = calcHeuristicCost(start[0],start[1],goal[0],goal[1])
#
#     while openNodes is not None:
#         openNodes = sorted(openNodes, key=lambda searchNode: searchNode.f)
#         currentNode = openNodes[0]
#         if currentNode.state == 'goal':
#             return reconstruct_path(cameFrom, current)
#
#         closedNodes.append(openNodes.pop(0))
#
#         for i < 4:
#             if i == 0:
#                 if openNodes == None
#                     i+=1
#                     break
#                 positionX = n. + 1
#             elif i == 1:
#                 if doesnt exits
#                     i+=1
#                     break
#                 positionX == n.psdjfg + 1
#                 positionY == asdlkjfsaddf
#             elif i == 2:
#                 if doesnt exits
#                     i+=1
#                     break
#                 positionX == n.psdjfg + 1
#             elif i == 3:
#                 if doesnt exits
#                     i+=1
#                     break
#                 positionX == n.psdjfg + 1
#             i += 1
#
#             for n in openNodes:
#                 if n.positionX == 1 && n.positionY == 22:
#                     sdjlkff
#             for n in closedNodes:
#                 if n.positionX == 1 && n.positionY == 22:
#                     sdjlkff
#             add to open nodes.
#     #Return a list of the nodes that exist in the shortes path
#     return None
#
# def calcHeuristicCost(currentNodeX,currentNodeY,goalNodeX,goalNodeY):
#     return abs(currentNodeX - goalNodeX) + abs(currentNodeY - goalNodeY)
