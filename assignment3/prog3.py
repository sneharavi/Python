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
 # Check upper diagonal on left side
   for i in range(len(board[0])):
      for j in range(len(board[0])):
         if abs(row-i) == abs(col-j):
            if i != row and j != col:
               if board[i][j]:
                  return False
   return True

def solveNQUtil(board,row):
   if row >= len(board[0]):
      return True
   col = randint(0, len(board)-1)
   for i in range(len(board)):
      if isSafe(board, row, col):
         board[row][col] = True
         if solveNQUtil(board, row+1):
            return True
         board[row][col] = False
      if isSafe(board, row, i):
         board[row][i] = True
         if solveNQUtil(board, row+1):
            return True
         board[row][i] = False
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