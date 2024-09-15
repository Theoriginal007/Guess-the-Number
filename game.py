import tkinter as tk
import random
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("500x500")
window.configure(bg="#2C3E50")  # Dark blue background

# Global variables
target_number = 0
attempts = 0
max_attempts = 0
remaining_attempts = 0
wins = 0
losses = 0

# Function to start a new game
def start_game(difficulty):
    global target_number, attempts, max_attempts, remaining_attempts
    attempts = 0
    entry.config(state='normal')
    check_button.config(state='normal')
    
    if difficulty == "Easy":
        target_number = random.randint(1, 50)
        max_attempts = 10
    elif difficulty == "Medium":
        target_number = random.randint(1, 100)
        max_attempts = 7
    else:  # Hard
        target_number = random.randint(1, 200)
        max_attempts = 5
    
    remaining_attempts = max_attempts
    result_label.config(text="", fg="#ECF0F1")
    attempts_label.config(text=f"Remaining Attempts: {remaining_attempts}", fg="#ECF0F1")
    entry.delete(0, tk.END)

# Function to check the guess
def check_guess():
    global attempts, remaining_attempts, wins, losses
    guess = entry.get()

    if not guess.isdigit():
        messagebox.showwarning("Invalid input", "Please enter a valid number!")
        entry.delete(0, tk.END)
        return

    guess = int(guess)
    attempts += 1
    remaining_attempts -= 1
    attempts_label.config(text=f"Remaining Attempts: {remaining_attempts}", fg="#ECF0F1")

    if guess < target_number:
        result_label.config(text="Too low! Try again.", fg="#F39C12")
    elif guess > target_number:
        result_label.config(text="Too high! Try again.", fg="#F39C12")
    else:
        result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.", fg="#2ECC71")
        entry.config(state='disabled')
        check_button.config(state='disabled')
        wins += 1
        update_scoreboard()
        return

    if remaining_attempts == 0:
        result_label.config(text=f"You lost! The number was {target_number}.", fg="#E74C3C")
        losses += 1
        update_scoreboard()
        entry.config(state='disabled')
        check_button.config(state='disabled')

# Function to reset the game
def reset_game():
    difficulty = difficulty_var.get()
    start_game(difficulty)

# Function to update the scoreboard
def update_scoreboard():
    scoreboard_label.config(text=f"Wins: {wins} | Losses: {losses}", fg="#ECF0F1")

# Add a label for difficulty selection
difficulty_var = tk.StringVar(value="Medium")
tk.Label(window, text="Select Difficulty:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1").pack(pady=10)
tk.Radiobutton(window, text="Easy (1-50)", variable=difficulty_var, value="Easy", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").pack()
tk.Radiobutton(window, text="Medium (1-100)", variable=difficulty_var, value="Medium", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").pack()
tk.Radiobutton(window, text="Hard (1-200)", variable=difficulty_var, value="Hard", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").pack()

# Add a button to start the game
start_button = tk.Button(window, text="Start Game", command=reset_game, font=("Arial", 14), bg="#3498DB", fg="#ECF0F1", bd=0, relief="flat", width=12)
start_button.pack(pady=20)

# Add a label for instructions
label = tk.Label(window, text="Guess the number:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(window, font=("Arial", 14), bg="#34495E", fg="#ECF0F1", justify="center", relief="flat", bd=2)
entry.pack(pady=10, ipadx=5, ipady=5)

# Add a button to check the guess
check_button = tk.Button(window, text="Check Guess", command=check_guess, font=("Arial", 14), bg="#3498DB", fg="#ECF0F1", bd=0, relief="flat", width=12, state='disabled')
check_button.pack(pady=20)

# Label to display the result of the guess
result_label = tk.Label(window, text="", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
result_label.pack(pady=10)

# Label to display remaining attempts
attempts_label = tk.Label(window, text="Remaining Attempts: ", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1")
attempts_label.pack(pady=10)

# Label to display the scoreboard
scoreboard_label = tk.Label(window, text="Wins: 0 | Losses: 0", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1")
scoreboard_label.pack(pady=10)

# Add a button to reset the game
reset_button = tk.Button(window, text="Reset Game", command=reset_game, font=("Arial", 14), bg="#E74C3C", fg="#ECF0F1", bd=0, relief="flat", width=12)
reset_button.pack(pady=20)

# Start the main loop
window.mainloop()
