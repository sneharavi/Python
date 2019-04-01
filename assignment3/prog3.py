#!/usr/bin/python3

from time import time
from random import seed, randint

def printBoard(board):
   for rowCount in range(0, len(board[0])):
      for columnCount in range(0, len(board[rowCount])):
         print("-"*7, end='')
      print()
      for columnCount in range(0, len(board[rowCount])):
         print("|      ", end='')
      print("|")
      for columnCount in range(0, len(board[rowCount])):
         if board[columnCount][rowCount]:
            queenString = "Q"
         else:
            queenString = " "
         print("|  %s   " % queenString, end='')
      print("|")
      for columnCount in range(0, len(board[rowCount])):
         print("|      ", end='')
      print("|")
   for columnCount in range(0, len(board[0])):
      print("-"*7, end='')
   print("")
   return

def isSafe(board, row, col): 
   # Check  for same column
   for i in range(len(board[0])):
      if board[i][col]:
         return False
   # Check for the same row
   for j in range(len(board[0])):
      if board[row][j]:
         return False
 # Check on both diagonals
   for i in range(len(board[0])):
      for j in range(len(board[0])):
         if abs(row-i) == abs(col-j):
            if i != row and j != col:
               if board[i][j]:
                  return False
   return True

def solveNQUtil(board,row):
    #check if we have eneterd the last row
   if row >= len(board[0]):
      return True
   # Consider a random column value on a row.
   col = randint(0, len(board)-1)
   #let go through all rows and columns in the marix
   for i in range(len(board)):
      # Check if my present location is safe.
      if isSafe(board, row, col):
         # save my present location as safe
         board[row][col] = True
         # now check for next row
         if solveNQUtil(board, row+1):
            return True
         # if next row is not safe then the present value I assumed  before
         # cannot give me a solution. Meaning I can cant place the queen..
         # So reset to False.
         board[row][col] = False
      # Try again for a new value in the same row continue till at least one
      # of the values succeed
      if isSafe(board, row, i):
         board[row][i] = True
         # if a queen can be placed in the next row,then proceed to find the solution.
         if solveNQUtil(board, row+1):
            return True
         # If solution was not found set the re-trying value back to False and try again
         board[row][i] = False
   # if no queen can be placed return false.
   return False

def solveNQueens(N):
   boardData = InitBoard(N)
   if solveNQUtil(boardData, 0):
      printBoard(boardData)
      return True
   else:
      print("Solution does not exist")

def InitBoard(N):
   seed(a=time(), version=2)
   boardArray = [[False for col in range(N)] for row in range(N)]
   return boardArray

def driver():
   for N  in range(1, 9):
      print("\nBoard size = %d" %  N)
      solveNQueens(N)

def main():
   """Main function"""
   return driver()

if __name__ == '__main__':
   main()
