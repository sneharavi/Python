#!/usr/bin/python3
"""
CSCI 503 - Assignment 3 - Spring 2019

Author: Sneha Ravi Chandran
Z-ID: z1856678
Date Due: March 21, 2019

Purpose: This program iterates through different
values of board size, detemine the solution to align N
Queen each of which in N rows without all of them lying
in the paths of each other.
"""
from time import time
from random import seed, randint

"""
Function Name:
   printBoard(board)

Description:
   Function prints the board array matrix into a board format
   with the queen represented by the letter 'Q'.
Parameters:
   None.

Returns:
   None
"""
def printBoard(board):
   # Print for all the cells in the board.
   for rowCount in range(len(board)):
      for columnCount in range(len(board)):
         # each row has 7 dashes per cell.
         print('-'*7, end='')
      # print newline at end of each row.
      print('')
      # print column spacing at end of each row.
      for columnCount in range(len(board)):
         print('|{:^6}'.format(' '), end='')
      # print border of the row.
      print('|')
      for columnCount in range(len(board)):
         # Pritn Q if a queen was found else print spaces.
         if board[columnCount][rowCount]:
            queenString = 'Q'
         else:
            queenString = ' '
         print('|{:^6}'.format(queenString), end='')
      print('|')
      # print lower half of the cell.
      for columnCount in range(len(board)):
         print('|{:^6}'.format(' '), end='')
      print('|')
   # print the bottom border of the board.
   for columnCount in range(len(board)):
      print("-"*7, end='')
   print('')
   return

"""
Function Name:
   isSafe(board, row, col):

Description:
   Function takes board data and the position of the queent to
   check for safety and detemines if there are not queens in the same
   column, same row and not in the diagonal paths.
   
Parameters:
   board - 2-D Array containing the positions of all the queens already placed.
   row - row in which the new queen is planned to be placed.
   col - column in which the new queen is planned to be placed.
   
Returns:
    Returns True if its safe to place the queen and False if its not safe.
"""
def isSafe(board, row, col):
   # Check  for same column
   for i in range(len(board)):
      # if a new queen was found in same column return False.
      if board[i][col]:
         return False
   # Check for the same row
   for j in range(len(board)):
      # if a new queen was found in same row return False.
      if board[row][j]:
         return False
 # Check upper diagonal on left side
   for i in range(len(board)):
      for j in range(len(board)):
         # All diagonal elements will be skewed equall hence
         # the difference between the rows and colums will be equal.
         if abs(row-i) == abs(col-j):
            # Do not have to compare against itself.
            if i != row and j != col:
               # if a queen is already found in one of the locations,
               # then the new queen cannot be palced so return False.
               if board[i][j]:
                  return False
   # if program reached here, then there were no queens found in the
   # same path as the one we are going to place.
   return True

"""
Function Name:
   solveNQUtil(board, row):

Description:
   Function takes board 2-D Array and row in which the queen is to be placed, it
   then iterates through the row to find solution in which queens can be placed by
   backtracking for already placed queens in the row before.
   
Parameters:
   board - 2-D Array containing the positions of all the queens already placed.
   row - row in which the new queen is planned to be placed.
   
Returns:
    Returns True if was able find a solution and place the queen, False if it
    cannot.
"""
def solveNQUtil(board, row):
   # if we reached end of board return True. This would mean we found
   # a solution and we were able to place the queens on all rows.
   if row >= len(board):
      return True
   # choose inital value of column randomly.
   col = randint(0, len(board)-1)
   for i in range(len(board)):
      # Check to see if the initlly chosen column is good to place a queen.
      if isSafe(board, row, col):
         # Set to True if its safe.
         board[row][col] = True
         # Check a solution is possible for the next row.
         # if yes then return to proceed for the solution on next row.
         if solveNQUtil(board, row+1):
            return True
         # If no queen can be placed for next row, remove the
         # already placed queen in the previous row - This would be termed
         # as backtracking.
         board[row][col] = False
      # Try again and find a possible row that would work for to attain the
      # solution of  placing the queen.
      if isSafe(board, row, i):
         # if we did find a solution  proceed to next row and check futher
         # solving of the puzzle is possible.
         board[row][i] = True
         # reset the saved position if the solution cannot be obtained anyhow.
         if solveNQUtil(board, row+1):
            return True
         board[row][i] = False
   # if no solution can be obtained return False.
   return False

"""
Function Name:
   solveNQueens()

Description:
   Function that takes size of board as argument and solves for placing N
   queens on a board of size N. If a solution is found it displays the board
   with the postion of all the queens marked, if not it print a message saying
   it could not find the solution ofr that particular size.
   
Parameters:
   N - Size of the board for which the solution is to be found.
   
Returns:
    Returns None.
"""
def solveNQueens(N):
   # Initialize the board with all cells set to false.
   boardData = initBoard(N)
   # Check if a solution can be obtained.
   if solveNQUtil(boardData, 0):
       # If a solution was found then print board data.
      printBoard(boardData)
   else:
      # if no solution was found  print the message saying so.
      print("Solution does not exist")
   return

"""
Function Name:
   initBoard()

Description:
   Function that takes size of board as argument, calls for random library
   seed and intializes for the board values. 
   
Parameters:
   N - Size of the board to be initialized for.
   
Returns:
    Returns a 2-D Array with all its values set to false.
"""
def initBoard(N):
   # Set up seed value. - seed(a=None, version=2) does the same as the line below.
   seed(a=time(), version=2)
   # set up a 2D  array for board with all its values set to False.
   boardArray = [[False for col in range(N)] for row in range(N)]
   # Return populated board array
   return boardArray

"""
Function Name:
   driver()

Description:
   Function runs the program to solve N queen on the board for values of N
   ranging from 1 to 8.
   
Parameters:
   None.
   
Returns:
    Returns None
"""
def driver():
   # Use for loop to iterate from 1 to 8.
   for N  in range(1, 9):
      print("\nBoard size = %d" %  N)
      # Call to solve for board size set to N
      solveNQueens(N)

"""
Function Name:
   main()

Description:
   Main function that call to solve for N queens
   
Parameters:
   
Returns:
    Returns None
"""
def main():
   """Main function"""
   driver()
   return

# set up for possible use as a package.
if __name__ == '__main__':
   main()
