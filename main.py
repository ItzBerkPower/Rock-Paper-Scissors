import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import ttk

# Open canvas
root = tk.Tk()

# Title of Game
root.title('Rock Paper Scissors')

# Size of Canvas
root.geometry("500x600")

# Background of Canvas
root.config(
    bg = "white"
)


# Rock, Paper, Scissors Images

rock_unsized = Image.open("rock.png")
rock_sized = rock_unsized.resize((458,242), Image.ANTIALIAS)
rock = ImageTk.PhotoImage(rock_sized)

paper_unsized = Image.open("paper.png")
paper_sized = paper_unsized.resize((458,242), Image.ANTIALIAS)
paper = ImageTk.PhotoImage(paper_sized)

scissors_unsized = Image.open("scissors.png")
scissors_sized = scissors_unsized.resize((458,242), Image.ANTIALIAS)
scissors = ImageTk.PhotoImage(scissors_sized)



# User Choice ---------------------------------------------

# Converting 

# Choice of the user
user_choice = ttk.Combobox(root, value = (
    "Rock",
    "Paper",
    "Scissors"
))

# Make sure the box isn't empty
user_choice.current(0)



#Robot Choice ------------------------------------------

#Add Images Into List
image_list = [rock, paper, scissors]

# Pick Random Integer in List

pick_number = random.randint(0, 2)

image_label = tk.Label(
    image = image_list[pick_number], 
    border = 0
)

# Spin Function
def spin():
    pick_number = random.randint(0,2)
    image_label.config(image = image_list[pick_number])

    #Converting Dropdowns into Numbers
    if user_choice.get() == "Rock":
        choice_value = 0
    
    elif user_choice.get() == "Paper":
        choice_value = 1
    
    elif user_choice.get() == "Scissors":
        choice_value = 2
    
    # If Rock Chosen (User)
    if choice_value == 0:
        if pick_number == 0:
            win_or_lose.config(text = "It's a tie! Spin Again.")
        elif pick_number == 1:
            win_or_lose.config(text = "You lost to the computer...")
        elif pick_number == 2:
            win_or_lose.config(text = "You beat the computer!")
    
    # If Paper Chosen (User)
    elif choice_value == 1:
        if pick_number == 0:
            win_or_lose.config(text = "You beat the computer!")
        elif pick_number == 1:
            win_or_lose.config(text = "Its a tie! Spin Again.")
        elif pick_number == 2:
            win_or_lose.config(text = "You lost to the computer...")

    #If Scissors Chosen (User)
    elif choice_value == 2:
        if pick_number == 0:
            win_or_lose.config(text = "You lost to the computer...")
        elif pick_number == 1:
            win_or_lose.config(text = "You beat the computer!")
        elif pick_number == 2:
            win_or_lose.config(text = "It's a tie! Spin Again")

# Button That Spins Game
spin_button = tk.Button(
    text = "Spin!",
    command = spin
)


# Seeing if Won Or Not -------------------------------------------------------
win_or_lose = tk.Label(
    root, 
    text = "", 
    font = ("Helvetica", 18),
    background = "white"
)


# Putting everything on screen

spin_button.pack(pady = 20)

image_label.pack(pady = 20)

user_choice.pack(pady = 20)

win_or_lose.pack(pady=50)

root.mainloop()
