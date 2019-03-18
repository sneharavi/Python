#!/usr/bin/python3

from time import time
from random import seed, randint

def isSafe(board, row, col): 
# Check this row on left side 
   for i in range(col): 
      if board[row][i] == 1: 
         return False

# Check upper diagonal on left side 
   for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
      if board[i][j] == 1: 
         return False

# Check lower diagonal on left side 
   for i,j in zip(range(row,N,1), range(col,-1,-1)): 
      if board[i][j] == 1: 
         return False

   return True

def solveNQueens (Data):
   return None

def InitBoard(N):
""" Initialize board."""
   boardArray  = [[0 for col in range(N)] for row in range(N)]
   return boardArray

def driver():
   for N  in range(1, 9):
      solveNQueens(InitBoard(N))

def main():
   """Main function"""
   return driver()

if __name__ == '__main__':
   main()
