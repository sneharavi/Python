#!/usr/bin/python3

from time import time
from random import seed, randint

def printBoard(board):
   print(board)

def isSafe(board, row, col): 
# Check this row on left side
   for i in range(col):
      if board[row][i] == 1:
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
      if isSafe(board, row, i):
         board[row][i] = 1
         if solveNQUtil(board, row+1):
            return True
         board[row][i] = 0
   return False

def solveNQueens (N):
   boardData = InitBoard(N)
   if solveNQUtil(boardData, 0) == False:
      print("Solution does not exist")
      return False
   printBoard(boardData)
   return True

def InitBoard(N):
   seed(a=None, version=2)
   row = randint(0, N)
   column = randint(0, N)
   boardArray = [[0 for col in range(N)] for row in range(N)]
   boardArray[row][column] = 1
   return boardArray

def driver():
   for N  in range(1, 9):
      solveNQueens(N)

def main():
   """Main function"""
   return driver()

if __name__ == '__main__':
   main()
   