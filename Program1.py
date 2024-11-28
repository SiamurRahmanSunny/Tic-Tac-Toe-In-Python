"""
Tic Tac Toe Game
Need Function winner board tie click
"""

#importing GUI
import tkinter as tk
from tkinter import messagebox

#Main Gui
root= tk.Tk()
root.geometry("600x600") #Width and Height
root.resizable(False, False) #blocking resize
root.title("Tic Tac Toe") #title of game
root.configure(bg="hot pink") #background color

#declaring variable
buttons = [[None for _ in range(3)]for _ in range(3)] #it's for buttons
player_turn = "X" #starting turn from X

#declaring functions

def winner_check(): #this for checking winner
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != " ":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != " ":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ": #cross left to right
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ": #cross right to left
        return True
    return False

def tie_check(): #this for checking tie
    for row in buttons:
        for button in row:
            if button["text"] == " ":
                return False
    return True

def reset_board(): #this for resetting board
    global player_turn
    player_turn = "X"
    for row in buttons:
        for button in row:
            button.config(text=" ", state=tk.NORMAL)

def click(row, col): #it's for clicking
    global player_turn #player_turn Variable
    print(f"Button clicked at {row}, {col}, Current Turn: {player_turn}")
    buttons[row][col].config(text=player_turn, state=tk.DISABLED)

    if winner_check(): #checking winner and showing message
        messagebox.showinfo("Game-Over", f" Player {player_turn} Becomes Genius Win The Game How!")
        print(f"Winner is {player_turn}")
        reset_board() #reset board
        print("Board Resetted")
    elif tie_check(): #checking tie and showing message
        messagebox.showinfo("Game-Over", "LOL No One Is Genius Match Tie")
        print("TIE")
        reset_board() #reset board
        print("Board Resetted")
    else:
        player_turn = "O" if player_turn == "X" else "X" #turning move. if player x move done then changing to O
        print(f"turn changed to {player_turn}")

def board(): #it's for Board Display
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=" ", bg="hot pink", fg="black", disabledforeground="black", font=("arial", 24), width="10", height="5", command=lambda r=row, c=col: click(r,c))
            button.grid(row=row, column=col)
            buttons[row][col] = button

board()

root.mainloop()