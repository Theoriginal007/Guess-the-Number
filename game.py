import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Guess the Number")

# Random number between 1 and 100
target_number = random.randint(1, 100)
attempts = 0

# Function to check the guess
def check_guess():
    global attempts
    attempts += 1
    guess = int(entry.get())
    
    if guess < target_number:
        result_label.config(text="Too low! Try again.")
    elif guess > target_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")

# Function to reset the game
def reset_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    entry.delete(0, tk.END)

# Add a label for instructions
label = tk.Label(window, text="Guess a number between 1 and 100:", font=("Arial", 14))
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Add a button to check the guess
check_button = tk.Button(window, text="Check Guess", command=check_guess, font=("Arial", 14))
check_button.pack(pady=10)

# Label to display the result of the guess
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Add a button to reset the game
reset_button = tk.Button(window, text="Play Again", command=reset_game, font=("Arial", 14))
reset_button.pack(pady=10)

window.mainloop()
