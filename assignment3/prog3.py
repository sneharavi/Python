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
   for columnCount in range(0, len(board[rowCount])):
      print("-"*7, end='')
   print("")
   return

def isSafe(board, row, col): 
# Check this row on left side
   for i in range(col):
      if board[row][col] == 1:
         return False

# Check upper diagonal on left side
   for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
      if board[i][j] == 1:
         return False

# Check lower diagonal on left side
   for i, j in zip(range(row, len(board[0]), 1), range(col, -1, -1)):
      if board[i][j] == 1:
         return False

   return True
 
def solveNQUtil(board,row):
   if row >= len(board[0]):
      return True
   for i in range(len(board[0])):
      col = randint(0, len(board[0]))
      if isSafe(board, row, col):
         board[row][col] = True
         if solveNQUtil(board, row+1):
            return True
         else:
            board[row][col] = False
   return False

def solveNQueens(N):
   boardData = InitBoard(N)
   if solveNQUtil(boardData, 0):
      print("Solution does not exist")
      return False
   printBoard(boardData)
   return True

def InitBoard(N):
   seed(a=None, version=2)
   boardArray = [[0 for col in range(N)] for row in range(N)]
   return boardArray

def driver():
   for N  in range(1, 9):
      print("Board size = %d" %  N)
      solveNQueens(N)

def main():
   """Main function"""
   return driver()

if __name__ == '__main__':
   main()
   