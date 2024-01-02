import tkinter as tk
from tkinter import messagebox

# Initialize game variables
current_player = 'X'
game_board = [' ']*9


# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

def button_click(index):
    global current_player
    if game_board[index] == ' ':
        game_board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif ' ' not in game_board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def reset_game():
    global current_player, game_board
    current_player = 'X'
    game_board = [' ']*9
    for button in buttons:
        button.config(text=' ', state=tk.NORMAL)


def check_winner():
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if game_board[condition[0]] == game_board[condition[1]] == game_board[condition[2]] != ' ':
            return True
    return False

    


# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 20), width=4, height=2,
                       command=lambda idx=i: button_click(idx))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)


root.mainloop()



