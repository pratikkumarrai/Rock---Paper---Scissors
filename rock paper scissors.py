import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")
window.configure(bg="lightblue")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# UI Components
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="lightblue")
title_label.pack(pady=20)

button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=15, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=15, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=15, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=30)

# Run the GUI loop
window.mainloop()
