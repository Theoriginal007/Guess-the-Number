import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("600x600")

# Global variables
target_number = 0
attempts = 0
max_attempts = 0
remaining_attempts = 0
wins = 0
losses = 0
theme = "default"
themes = {
    "Default": {"bg": "#2C3E50", "fg": "#ECF0F1", "button_bg": "#3498DB", "button_fg": "#ECF0F1", "entry_bg": "#34495E", "entry_fg": "#ECF0F1"},
    "Light": {"bg": "#FFFFFF", "fg": "#2C3E50", "button_bg": "#3498DB", "button_fg": "#FFFFFF", "entry_bg": "#E0E0E0", "entry_fg": "#2C3E50"},
    "Dark": {"bg": "#121212", "fg": "#F5F5F5", "button_bg": "#BB86FC", "button_fg": "#121212", "entry_bg": "#2C2C2C", "entry_fg": "#F5F5F5"},
}

# Function to apply the selected theme
def apply_theme(selected_theme):
    theme_data = themes[selected_theme]
    window.config(bg=theme_data["bg"])
    label.config(bg=theme_data["bg"], fg=theme_data["fg"])
    entry.config(bg=theme_data["entry_bg"], fg=theme_data["entry_fg"])
    check_button.config(bg=theme_data["button_bg"], fg=theme_data["button_fg"])
    reset_button.config(bg=theme_data["button_bg"], fg=theme_data["button_fg"])
    attempts_label.config(bg=theme_data["bg"], fg=theme_data["fg"])
    result_label.config(bg=theme_data["bg"], fg=theme_data["fg"])
    scoreboard_label.config(bg=theme_data["bg"], fg=theme_data["fg"])
    leaderboard_label.config(bg=theme_data["bg"], fg=theme_data["fg"])

# Function to open settings window
def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("400x300")
    settings_window.config(bg=themes[theme]["bg"])

    tk.Label(settings_window, text="Select Theme:", font=("Arial", 14), bg=themes[theme]["bg"], fg=themes[theme]["fg"]).pack(pady=20)

    # Theme selection dropdown
    theme_var = tk.StringVar(value=theme)
    theme_dropdown = tk.OptionMenu(settings_window, theme_var, *themes.keys(), command=apply_theme)
    theme_dropdown.config(font=("Arial", 12), bg=themes[theme]["button_bg"], fg=themes[theme]["button_fg"], width=10)
    theme_dropdown.pack(pady=10)

# Function to start a new game
def start_game(difficulty):
    global target_number, attempts, max_attempts, remaining_attempts
    attempts = 0
    entry.config(state='normal')
    check_button.config(state='normal')

    # Set target number and max attempts based on difficulty
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
    result_label.config(text="")
    attempts_label.config(text=f"Remaining Attempts: {remaining_attempts}")

# Function to check the guess
def check_guess():
    global attempts, remaining_attempts, wins, losses
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="Invalid input, enter a number!")
        entry.delete(0, tk.END)
        return

    guess = int(guess)
    attempts += 1
    remaining_attempts -= 1
    attempts_label.config(text=f"Remaining Attempts: {remaining_attempts}")

    # Check if guess is correct, too high, or too low
    if guess < target_number:
        result_label.config(text="Too low! Try again.")
    elif guess > target_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")
        entry.config(state='disabled')
        check_button.config(state='disabled')
        wins += 1
        update_scoreboard()
        return

    # Check if attempts are exhausted
    if remaining_attempts == 0:
        result_label.config(text=f"You lost! The number was {target_number}.")
        losses += 1
        entry.config(state='disabled')
        check_button.config(state='disabled')

# Function to reset the game
def reset_game():
    difficulty = difficulty_var.get()
    start_game(difficulty)

# Function to update the scoreboard
def update_scoreboard():
    scoreboard_label.config(text=f"Wins: {wins} | Losses: {losses}")

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

# Label to display the leaderboard
leaderboard_label = tk.Label(window, text="Leaderboard:\nNo scores yet.", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1")
leaderboard_label.pack(pady=10)

# Add a button to reset the game
reset_button = tk.Button(window, text="Reset Game", command=reset_game, font=("Arial", 14), bg="#E74C3C", fg="#ECF0F1", bd=0, relief="flat", width=12)
reset_button.pack(pady=20)

# Add a button to open settings
settings_button = tk.Button(window, text="Settings", command=open_settings, font=("Arial", 14), bg="#8E44AD", fg="#ECF0F1", bd=0, relief="flat", width=12)
settings_button.pack(pady=10)

# Start the main loop
apply_theme("Default")  # Apply the default theme on startup
window.mainloop()
