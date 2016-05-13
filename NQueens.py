# Trying to solve n queens , starting with 4x4


#


def CloneBoard( board ) :
    newBoard = []
    
    boardSize = len(board)
    
    for  row in range( 0 , boardSize )  : 
        newBoard.append( [] )
        for x in range( 0 , boardSize ) :
            newBoard[row].append( board[row][x] )    
    
    return newBoard
    




def UpdateItem( board , xPos ,yPos , value ) :
    board[yPos][xPos] = value 
    return board
 
 
def GetItem( board ,xPos , yPos ) :
    
    size = len( board )
    
    if xPos > size :
        print " X to large at " + xPos
        return "F"
    
    if yPos > size :
        print " Y to large at " + yPos
        return "F"
    
    
    return board[yPos][xPos]
 
def generateBoard( size ) :
    newBoard = []
    for row in range( 0 ,size ) :
        newBoard.append( [] )
        for x in range( 0 , size ) : 
            newBoard[row].append( "o" )
    return newBoard

def printBoardState( board ) :
    for va in board :
        rowState = "";
        for state in va :
            rowState += state
        print rowState

def placeQueen( board ,xPos , yPos  ) :
    board = UpdateItem( board , xPos , yPos , 'q' )
    markQueensZone( board ,xPos , yPos )
    return board


# Mark of the squares no longer eligibile for positions
def markQueensZone( board , xPos , yPos ) :
    board = markVertical( board , xPos , yPos   )    
    board = markPosAxis( board ,xPos , yPos )
    board = markNegAxis( board ,xPos , yPos )

# Only need to mark downwards due to algo
def markVertical( board , xPos , yPos  ) : 
    for column in range( yPos  + 1, len( board ) )  :
        board = UpdateItem( board , xPos , column , 'x' )
    return board

def markPosAxis( board , xPos , yPos ) : 
    boardSize = len( board )
    
    # mark \  
    dX = xPos + 1
    dY = yPos + 1
    while ( dX < boardSize and dY < boardSize ) :
        board = UpdateItem( board , dX , dY , 'x' )
        dX = dX + 1
        dY = dY + 1
    
    return board
 
def markNegAxis( board , xPos , yPos ) : 
    boardSize = len( board )
    
    # mark /  
    dX = xPos - 1
    dY = yPos + 1
    while ( dX > -1 and dY < boardSize ) :
        board = UpdateItem( board , dX , dY , 'x' )
        dX = dX - 1
        dY = dY + 1
    
    return board
 

globalCount = 0

def findSolution( currentBoard , currentY ) :

    if  currentY >= len(currentBoard ) :
        print "Solution found "
        global globalCount
        globalCount = globalCount + 1
        print "\n"
        return True
        
    # Go through each element in the row
    # If its free place a queen there and pass on that board state for the nextCol
    newBoard  = []
    boardSize = len( currentBoard )
    for row in range( 0 , boardSize)  :
        spaceVal = GetItem( currentBoard ,row , currentY )
        
        if spaceVal == "F" :
            return
        
        if spaceVal == "o" : 
            newBoard = CloneBoard( currentBoard )
            newBoard = placeQueen( newBoard , row, currentY )
            findSolution( newBoard , currentY + 1)
            
    return False



def main() :
    board = generateBoard( 8 )
    findSolution( board , 0)
    print globalCount
    

main()