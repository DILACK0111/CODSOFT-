import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def user_select(selection):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(selection, computer_choice)
    label_result.config(text=f"Computer chose: {computer_choice}\n{result}")

# Creating the GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

frame = tk.Frame(root)
frame.pack()

label_title = tk.Label(frame, text="Select your choice:")
label_title.pack()

button_rock = tk.Button(frame, text="Rock", command=lambda: user_select("rock"))
button_rock.pack()

button_paper = tk.Button(frame, text="Paper", command=lambda: user_select("paper"))
button_paper.pack()

button_scissors = tk.Button(frame, text="Scissors", command=lambda: user_select("scissors"))
button_scissors.pack()

label_result = tk.Label(frame, text="")
label_result.pack()

root.mainloop()
