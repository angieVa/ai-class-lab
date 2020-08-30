import re
from random import randint

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)

    over = False
    if (self.board[0] == _PLAYER_SYMBOL and self.board[1] == _PLAYER_SYMBOL and self.board[2] == _PLAYER_SYMBOL): #rowPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[3] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL): #rowPlayer
      self.winner = _PLAYER
      over = True
    elif(self.board[6] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL): #rowPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[1] == _MACHINE_SYMBOL and self.board[2] == _MACHINE_SYMBOL): #rowMachine
      self.winner = _MACHINE
      over = True
    elif (self.board[3] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL): #rowMachine
      self.winner = _MACHINE
      over = True
    elif(self.board[6] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL): #rowMachine
      self.winner = _MACHINE
      over = True
    elif (self.board[0] == _PLAYER_SYMBOL and self.board[3] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL): #columnPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[1] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL): #columnPlayer
      self.winner = _PLAYER
      over = True
    elif(self.board[2] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL): #columnPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[3] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL): #columnMachine
      self.winner = _MACHINE
      over = True
    elif (self.board[1] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL): #columnMachine
      self.winner = _MACHINE
      over = True
    elif(self.board[2] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL): #columnMachine
      self.winner = _MACHINE
      over = True
    elif (self.board[0] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL): #diagonalPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[2] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL): #diagonalPlayer
      self.winner = _PLAYER
      over = True
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL): #diagonalMachine
      self.winner = _MACHINE
      over = True
    elif (self.board[2] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL): #diagonalMachine
      self.winner = _MACHINE
      over = True
    elif self.board.count(None) == 0:
      self.winner = "Nobody"
      over = True

    return over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied

    choose = False
    cell = randint(0, 8)
    while not choose:
       if self.board[cell] is not None:
         cell = randint(0, 8)
       else:
         self.board[cell] = _MACHINE_SYMBOL
         choose = True

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    print("The winner is: " + self.winner)
    
