# N Queens solution
import sys

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
    board = markAxis( board , xPos , yPos , 1 , PosAxisCheck )
    board = markAxis( board , xPos , yPos , -1 , NegAxisCheck  )
    return board
     
# Only need to mark downwards due to algo
def markVertical( board , xPos , yPos  ) : 
    for column in range( yPos  + 1, len( board ) )  :
        board = UpdateItem( board , xPos , column , 'x' )
    return board

def PosAxisCheck( x , size ) :
     return x < size 

def NegAxisCheck( x , size ) :       
    return x > -1

def markAxis( board , xPos , yPos , xAlt , xCheck ) : 
    boardSize = len( board )
    
    dX = xPos + xAlt
    dY = yPos + 1
    while ( xCheck( dX , boardSize ) and dY < boardSize ) :
        board = UpdateItem( board , dX , dY , 'x' )
        dX = dX + xAlt
        dY = dY + 1
    
    return board

 

globalCount = 0

def findSolution( currentBoard , currentY ) :

    if  currentY >= len(currentBoard ) :
        global globalCount
        globalCount = globalCount + 1
        return
        
    # Go through each element in the row
    # If its free place a queen there and pass on that board state for the nextCol
    newBoard  = []
    boardSize = len( currentBoard )
    for row in range( 0 , boardSize)  :           
        if GetItem( currentBoard ,row , currentY ) == "o" : 
            newBoard = CloneBoard( currentBoard )
            newBoard = placeQueen( newBoard , row, currentY )
            findSolution( newBoard , currentY + 1)
    return 



def main() :

    boardSize = sys.argv[1]
    
    board = generateBoard( int( boardSize ) )
    findSolution( board , 0)
    print "Number of solutions = " + str(globalCount)
    

main()