# author: Cheuk Yan Cherry Li
# date: October 22, 2022
# file: board.py a Python program that implements a tic-tac-toe game board

class Board:
      def __init__(self):
            # initial cells represent as " "
            self.sign = " "
            # 3*3 board
            self.size = 3
            # list of initial cells
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      
      def get_size(self): 
            # return the board size (an instance size)
            return self.size

      def get_winner(self):
            # return the winner's sign O or X (an instance winner)
            return self.winner
                 
      def set(self, cell, sign): 
            # mark the cell with X or O
            cellTuple = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
            index = cellTuple.index(cell)
            self.board[index] = sign

      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            cellTuple = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
            index = cellTuple.index(cell)
            if self.board[index] == " ":
                  return True
            return False

      def isdone(self):
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            done = False
            self.winner = ''

            # diagonal case
            if self.board[0]==self.board[4]==self.board[8]!=' ':
                  done = True
                  self.winner = self.board[0]
            elif self.board[2]==self.board[4]==self.board[6]!=' ':
                  done = True
                  self.winner = self.board[2]

            # row case
            elif self.board[0]==self.board[1]==self.board[2]!=' ':
                  done = True
                  self.winner = self.board[0]
            elif self.board[3]==self.board[4]==self.board[5]!=' ':
                  done = True
                  self.winner = self.board[3]
            elif self.board[6]==self.board[7]==self.board[8]!=' ':
                  done = True
                  self.winner = self.board[6]

            # column case
            elif self.board[0]==self.board[3]==self.board[6]!=' ':
                  done = True
                  self.winner = self.board[0]
            elif self.board[1]==self.board[4]==self.board[7]!=' ':
                  done = True
                  self.winner = self.board[1]
            elif self.board[2]==self.board[5]==self.board[8]!=' ':
                  done = True
                  self.winner = self.board[2]

            # tie
            elif self.board[0]!=' ' and self.board[1]!=' ' and self.board[2]!=' ' and self.board[3]!=' ' and self.board[4]!=' ' and self.board[5]!=' ' and self.board[6]!=' ' and self.board[7]!=' ' and self.board[8]!=' ':
                  done = True
                  self.winner = ""

            return done
     

      def show(self):
            # draw the board
            oddRow = "+---+---+---+"
            one = "| "+ self.board[0] + " | "+ self.board[1] + " | "+ self.board[2] + " |"
            two = "| "+ self.board[3] + " | "+ self.board[4] + " | "+ self.board[5] + " |"
            three = "| "+ self.board[6] + " | "+ self.board[7] + " | "+ self.board[8] + " |"

            print("   A   B   C")
            print(" " + oddRow)
            print("1"+ one)
            print(" " + oddRow)
            print("2"+ two)
            print(" " + oddRow)
            print("3"+ three)
            print(" " + oddRow)