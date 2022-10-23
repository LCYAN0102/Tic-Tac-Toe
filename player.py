# author: Cheuk Yan Cherry Li
# date: October 22, 2022
# file: player.py a Python program that implements a player, a simpleAI, Minimax AI, and SmartAI for tic-tac-toe game

import random
from random import choice
from numpy import inf

class Player:
      def __init__(self, name, sign):
            # player's name
            self.name = name  
            # player's sign O or X
            self.sign = sign  

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            while 1:
                  # prompt the user to choose a cell
                  cell = input(self.name + ", " + self.sign + ": " + "Enter a cell [A-C][1-3]: " + "\n").upper()
                  letter = ("a", "b", "c", "A", "B", "C")
                  num = ("1", "2", "3")

                  # check user input and update the board
                  if len(cell) == 2 and cell[0] in letter and cell[1] in num and board.isempty(cell) == True:
                        board.set(cell, self.sign)
                        break 
                  else:
                        print("You did not choose correctly.")

# An AI that choose a random cell
class AI(Player):
      def __init__(self, name, sign, board):
            self.board = board
            super().__init__(name, sign)

      def choose(self, board):
            # choose a random empty cell
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            while 1:
                  cellList = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
                  cell = choice(cellList)
                  if board.isempty(cell) == True:
                        board.set(cell, self.sign)
                        print(cell)
                        break

# MiniMax that uses a minimax algorithm based on recursion
class MiniMax(AI):
      def __init__(self, name, sign, board):
          #  self.board = board
            super().__init__(name, sign, board)

      # choose a empty cell according to minimax algorithm
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      # minimax algorithm
      def minimax(self, board, self_player, start):
            # check the sign
            if self.sign == "O":
                  opponentSign = "X"
            else:
                  opponentSign = "O"

            # check the base conditions
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
                  # is a tie
                  elif board.get_winner() == "":
                        return 0
                  # self is a loser (opponent is a winner)
                  else:
                        return -1

            maxScore = -inf
            minScore = inf
            move = ""
            cellList = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

            # calculate the best cell
            for item in cellList:
                  if board.isempty(item) == True:
                        if self_player == True:
                              board.set(item, self.sign)
                              score = MiniMax.minimax(self, board, False, False)
                              if score > maxScore:
                                    maxScore = score
                                    move = item
                              board.set(item, " ")

                        else:
                              board.set(item, opponentSign)
                              score = MiniMax.minimax(self, board, True, False)
                              if score < minScore:
                                    minScore = score
                                    move = item
                              board.set(item, " ")

                        
            if start:
                  return move
            elif self_player:
                  return maxScore
            else:
                  return minScore

# A smartAI that use a simple heuristic approach to check all possible winning conditions
class SmartAI(AI):
      def __init__(self, name, sign, board):
         #   self.board = board
            super().__init__(name, sign, board)

      # choose a empty cell by checking all possible winning conditions
      def choose(self, board):
            move = ""
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")

            # check the signs
            if self.sign == "O":
                  opponentSign = "X"
            else:
                  opponentSign = "O"

            # get the updated empty cell list
            cellList = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            emptyCell = []
            for item in cellList:
                  if board.isempty(item) == True:
                        emptyCell.append(item)

            # win the game or block the opponent from winning
            for player in [self.sign, opponentSign]:
                  for item in emptyCell:
                        board.set(item, player)
                        if board.isdone():
                              move = item
                              board.set(item, self.sign)
                              print(move)
                              return
                        else:
                              board.set(item, " ")

            # winning stategy if the smartAI goes first
            if len(emptyCell) % 2 == 1:
                  # choose a empty random corner cell
                  corner = ["A1", "C1", "A3", "C3"]
                  emptyCorners = []
                  for item in corner:
                        if board.isempty(item) == True:
                              emptyCorners.append(item)
                  if len(emptyCorners) > 0:
                        move = choice(emptyCorners)
                        board.set(move, self.sign)
                        print(move)
                        return
                  
                  # choose the center
                  if board.isempty("B2") == True:
                        move = "B2"
                        board.set(move, self.sign)
                        print(move)
                        return
                  
                  # choose a empty random cell other than corner and center
                  other = ["B1", "A2", "C2", "B3"]
                  emptyOther = []
                  for item in other:
                        if board.isempty(item) == True:
                              emptyOther.append(item)
                  if len(emptyOther) > 0:
                              move = choice(emptyOther)
                              board.set(move, self.sign)
                              print(move)
                              return

            # winning stategy if the smartAI goes second
            else:
                  # choose the center
                  if board.isempty("B2") == True:
                        move = "B2"
                        board.set(move, self.sign)
                        print(move)
                        return

                  # choose a empty random corner cell if there are more than 2 empty corner cells
                  corner = ["A1", "C1", "A3", "C3"]
                  emptyCorners = []
                  for item in corner:
                        if board.isempty(item) == True:
                              emptyCorners.append(item)
                  if len(emptyCorners) > 2:
                        move = choice(emptyCorners)
                        board.set(move, self.sign)
                        print(move)
                        return
                                    
                  # choose a empty random cell other than corner and center
                  other = ["B1", "A2", "C2", "B3"]
                  emptyOther = []
                  for item in other:
                        if board.isempty(item) == True:
                              emptyOther.append(item)
                  if len(emptyOther) > 0:
                              move = choice(emptyOther)
                              board.set(move, self.sign)
                              print(move)
                              return