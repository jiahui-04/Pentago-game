import numpy as np
import random


def display_board(board):
       
    board_1 = ""
    row_number = 0
    for row in board:
        for index, number in enumerate(row):
            if index == 2:
                board_1 += f" {number} "
                board_1 += " | "
            else:
                board_1 += f" {number} "
        board_1 += "\n"
        if row_number == 2:
            board_1 += " "
            board_1 += "—" * 19
            board_1 += "\n"
        row_number += 1
    board = board_1
    print(board)
    
    pass
        
def check_victory(board, turn, rot):
      
      board = board.copy()
      save_winp1 = False
      save_winp2 = False
     
     #undo rotation
      if rot == 2:
           board[:3, 3:] = np.rot90(board[:3, 3:], 3)
      elif rot == 1:
           board[:3, 3:] = np.rot90(board[:3, 3:], 1)
      elif rot == 4:
           board[3:, 3:] = np.rot90(board[3:, 3:], 3)
      elif rot == 3:
           board[3:, 3:] = np.rot90(board[3:, 3:], 1)
      elif rot == 6:
           board[3:, :3] = np.rot90(board[3:, :3], 3)
      elif rot == 5:
           board[3:, :3] = np.rot90(board[3:, :3], 1)
      elif rot == 8:
           board[:3, :3] = np.rot90(board[:3, :3], 3)
      elif rot == 7:
           board[:3, :3] = np.rot90(board[:3, :3], 1)
     
      #check victory before rotation  
      #check if first 5 or last 5 positions in a row have the same colour marble
      for row in board:
           if (row[:5] == 1).all() or (row[1:] == 1).all():
               save_winp1 = True
           if (row[:5] == 2).all() or (row[1:] == 2).all():
               save_winp2 = True
      
      #check if first 5 or last 5 positions in a column have the same colour marble
      for col in board.T:
         if (col[:5] == 1).all() or (col[1:] == 1).all():
               save_winp1 = True
         if (col[:5] == 2).all() or (col[1:] == 2).all():
              save_winp2 = True 
     
      #check if 5 consecutive positions in all possible diagonals have the same
      #colour marble
      if (board[(0,1,2,3,4), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(1,2,3,4,5), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(1,2,3,4,5), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(0,1,2,3,4), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(4,3,2,1,0), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(5,4,3,2,1), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(4,3,2,1,0), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(5,4,3,2,1), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
       
      if (board[(0,1,2,3,4), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(1,2,3,4,5), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(1,2,3,4,5), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(0,1,2,3,4), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(4,3,2,1,0), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(5,4,3,2,1), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(4,3,2,1,0), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(5,4,3,2,1), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
       
      #apply rotation
      if rot == 1:
           board[:3, 3:] = np.rot90(board[:3, 3:], 3)
      elif rot == 2:
           board[:3, 3:] = np.rot90(board[:3, 3:], 1)
      elif rot == 3:
           board[3:, 3:] = np.rot90(board[3:, 3:], 3)
      elif rot == 4:
           board[3:, 3:] = np.rot90(board[3:, 3:], 1)
      elif rot == 5:
           board[3:, :3] = np.rot90(board[3:, :3], 3)
      elif rot == 6:
           board[3:, :3] = np.rot90(board[3:, :3], 1)
      elif rot == 7:
           board[:3, :3] = np.rot90(board[:3, :3], 3)
      elif rot == 8:
           board[:3, :3] = np.rot90(board[:3, :3], 1)
       
      #check victory after rotation
      for row in board:
          if (row[:5] == 1).all() or (row[1:] == 1).all():
              save_winp1 = True
          if (row[:5] == 2).all() or (row[1:] == 2).all():
              save_winp2= True
          
      for col in board.T:
          if (col[:5] == 1).all() or (col[1:] == 1).all():
              save_winp1 = True
          if (col[:5] == 2).all() or (col[1:] == 2).all():
              save_winp2= True
     
      if (board[(0,1,2,3,4), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(1,2,3,4,5), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(1,2,3,4,5), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(0,1,2,3,4), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(4,3,2,1,0), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(5,4,3,2,1), (0,1,2,3,4)] == 1).all():
          save_winp1 = True
      if (board[(4,3,2,1,0), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      if (board[(5,4,3,2,1), (1,2,3,4,5)] == 1).all():
          save_winp1 = True
      
      if (board[(0,1,2,3,4), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(1,2,3,4,5), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(1,2,3,4,5), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(0,1,2,3,4), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(4,3,2,1,0), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(5,4,3,2,1), (0,1,2,3,4)] == 2).all():
          save_winp2 = True
      if (board[(4,3,2,1,0), (1,2,3,4,5)] == 2).all():
          save_winp2 = True
      if (board[(5,4,3,2,1), (1,2,3,4,5)] == 2).all():
          save_winp2 = True          
              
      #draw or continue
      draw=np.all(board != 0)
      if save_winp1 == True:
          return 1
      if save_winp2 == True:
          return 2
      if draw or (save_winp1 == True and save_winp2 == True):
          return 3
       
      return 0

def apply_move(board, turn, row, col, rot):
    
    board = board.copy()
    board[row, col] = turn
    
    #apply rotation
    if rot == 1:
        board[:3, 3:] = np.rot90(board[:3, 3:], 3)
    elif rot == 2:
        board[:3, 3:] = np.rot90(board[:3, 3:], 1)
    elif rot == 3:
        board[3:, 3:] = np.rot90(board[3:, 3:], 3)
    elif rot == 4:
        board[3:, 3:] = np.rot90(board[3:, 3:], 1)
    elif rot == 5:
        board[3:, :3] = np.rot90(board[3:, :3], 3)
    elif rot == 6:
        board[3:, :3] = np.rot90(board[3:, :3], 1)
    elif rot == 7:
        board[:3, :3] = np.rot90(board[:3, :3], 3)
    elif rot == 8:
        board[:3, :3] = np.rot90(board[:3, :3], 1)
        
    return board
    
def check_move(board, row, col):    
   
    #check if position is occupied
    if board[row, col] != 0:
        print("Position is already occupied. Please choose another position.")
        return False
    else:
        return True

def computer_move(board, turn, level):
    
    #computer apply random valid move
    if level == 1:
        possiblemove = []
        for row in range(6):
            for col in range(6):
                for rot in range(1,9):
                    if board[row][col] == 0:
                        possiblemove.append((row,col,rot))
        return random.choice(possiblemove)
    
    #computer apply smart move
    if level == 2:
        smartmove = []
        possiblemove = []
        for row in range(6):
            for col in range(6):
                for rot in range(1,9):
                    if board[row][col] == 0:
                        possiblemove.append((row,col,rot))
                        #computer apply winning move
                        computer_board = board.copy()
                        computer_board = apply_move(computer_board, turn, row, col, rot)
                        if check_victory(computer_board, turn, rot) == turn:
                            return (row, col, rot)
        
        #shuffle the list of possiblemove
        random.shuffle(possiblemove)
        
        #computer creates a copy of the board and apply possiblemove
        for row,col,rot in possiblemove:
            if board[row][col] == 0:
                computer_board = board.copy()
                computer_board = apply_move(computer_board, turn, row, col, rot)
                bad_move = False 
                opponent = 3 - turn 
     
                #computer check for opponent's potential winning move
                for opp_row, opp_col, opp_rot in possiblemove:
                    if computer_board[opp_row][opp_col] == 0:
                        opponent_board = computer_board.copy()
                        opponent_board = apply_move(opponent_board, opponent, opp_row, opp_col, opp_rot)
                        #if opponent can win, move is bad
                        if check_victory(opponent_board, opponent, opp_rot) == opponent:
                            bad_move = True
                            break
                
                #if move is not bad, add it to the list of smartmove
                if not bad_move:
                    smartmove.append((row, col, rot))
                    return (row,col,rot)
        
        #if no winning and smart move, computer apply random valid move
        return random.choice(possiblemove)

def menu():  
    print("Welcome to Pentago!")
    print("PVP -- Player vs Player \nPVC -- Player vs Computer")
    
    while True: 
        user_input = input("PVP or PVC? ")
        if user_input != 'PVP' and user_input != 'PVC':
            print("Invalid input.")
            continue
        else:
            break
    
    
    if user_input == 'PVP':
        pass
    else:
        print("Level 1 -- Easy \nLevel 2 -- Medium")
        while True:
            level_input = input("Please input difficulty level -- 1 or 2. ")
            try:
                level = int(level_input)
                if level != 1 and level != 2:
                    print("Invalid input. Input 1 or 2 only.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer -- 1 or 2.")
                continue
    
    print("Game Start!")
    game_board = np.zeros((6,6))
    game_board = game_board.astype(int)
    turn = 1 
   
   
    while True:
        display_board(game_board)
        
        print("Player",turn,"'s turn:")
        if user_input == 'PVP' or (user_input == 'PVC' and turn == 1):
            try:
                row = int(input("Row: Please select an integer from 0 to 5. "))
                col = int(input("Col: Please select an integer from 0 to 5. "))
                rot = int(input("Rot: Please select an integer from 1 to 8. "))
                if row < 0 or row > 5 or col < 0 or col > 5 or rot < 1 or rot > 8:
                    print("Invalid move. Please select an integer in the given range.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
                
        else:
            row, col, rot = computer_move(game_board, turn, level)

        if check_move(game_board, row, col) == True:
            game_board = apply_move(game_board, turn, row, col, rot)
        else: 
            continue

        victory_result = check_victory(game_board, turn, rot)
        if victory_result == 1:
            print("Player 1 wins!")
            display_board(game_board)
            break
        elif victory_result == 2:
            print("Player 2 wins!")
            display_board(game_board)
            break
        elif victory_result == 3:
            print("Draw.")
            display_board(game_board)
            break
        turn = 3 - turn
         
    
    pass

if __name__ == "__main__":
    menu()




