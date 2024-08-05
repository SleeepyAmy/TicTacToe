# hello mwah 

import tkinter # tk-interface OR smth

def set_tile(row, column):
    global curr_player

    # if the game is over or the tile is already taken, we can't place anything there so thats what are we gonna do next 

    if game_over or board[row][column]["text"] != "":
        return

    # Put the current player's mark (X or O) on the chosen tile
    board[row][column]["text"] = curr_player

    # Now let's switch players just like how we gonna switch Gege's bones if choso died
    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = curr_player + "'s turn"

    # Time to check if someone actully smart and slayed the game and won 
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Check horizontally
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " you SLAYED wow weam is proud", foreground=color_black)
            for column in range(3):
                board[row][column].config(foreground=color_black, background=color_light_purple)
            game_over = True
            return
    
    # Check vertically=
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " you SLAYED wow weam is proud", foreground=color_black)
            for row in range(3):
                board[row][column].config(foreground=color_black, background=color_light_purple)
            game_over = True
            return
    
    # Check diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " you SLAYED wow weam is proud", foreground=color_black)
        for i in range(3):
            board[i][i].config(foreground=color_black, background=color_light_purple)
        game_over = True
        return

    # Check anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " you SLAYED wow weam is proud", foreground=color_black)
        board[0][2].config(foreground=color_black, background=color_light_purple)
        board[1][1].config(foreground=color_black, background=color_light_purple)
        board[2][0].config(foreground=color_black, background=color_light_purple)
        game_over = True
        return
    
    # If all spots are filled and no winner, it's a tie
    if turns == 9:
        game_over = True
        label.config(text=" you guys are dumb or smart", foreground=color_black)

def new_game():
    global turns, game_over

    # Reset the game for a fresh start
    turns = 0
    game_over = False

    label.config(text=curr_player + "'s turn", foreground="black")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_dark, background=color_purple)

# Game setup and stuff
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

#  ofc its purple colors for my TTt game
color_dark = "#51414F"
color_black = "black"
color_purple = "#E0B0FF"
color_light_purple = "#915F6D"

turns = 0
game_over = False

# Window setup
window = tkinter.Tk() # Create the game window
window.title(" WEAM GREATEST TIC TAC TOE ")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_purple,
                      foreground="black")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_purple, foreground=color_dark, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_purple,
                        foreground="black", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window 
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# Format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Start the main event 
window.mainloop()

