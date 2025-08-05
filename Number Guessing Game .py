import tkinter as tk
from tkinter import messagebox
import random

# Global variables
secret_number = 0
attempts = 0
max_attempts = 7

def start_new_game():
    """Start a new game by generating a random number"""
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_result.config(text="I'm thinking of a number between 1 and 100!")
    label_attempts.config(text=f"Attempts left: {max_attempts}")
    button_guess.config(state="normal")
    entry_guess.config(state="normal")

def make_guess():
    """Handle the player's guess"""
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1
        attempts_left = max_attempts - attempts

        if guess == secret_number:
            label_result.config(text=f"🎉 Congratulations! You got it in {attempts} attempts!")
            button_guess.config(state="disabled")
            entry_guess.config(state="disabled")
        elif attempts >= max_attempts:
            label_result.config(text=f"❌ Game Over! The number was {secret_number}")
            button_guess.config(state="disabled")
            entry_guess.config(state="disabled")
        elif guess < secret_number:
            label_result.config(text="Too low! Try a higher number.")
        else:
            label_result.config(text="Too high! Try a lower number.")

        label_attempts.config(text=f"Attempts left: {attempts_left}")
        entry_guess.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")
        entry_guess.delete(0, tk.END)

def on_enter_key(event):
    """Allow pressing Enter to make a guess"""
    make_guess()

def create_window():
    """Create and set up the main game window"""
    global entry_guess, label_result, label_attempts, button_guess

    window = tk.Tk()
    window.title("Number Guessing Game")
    window.geometry("400x370")
    window.configure(bg="#2c3e50")  # Formal dark blue-gray background

    # Title
    title_label = tk.Label(window, text="Number Guessing Game", font=("Arial", 18, "bold"),
                           bg="#2c3e50", fg="#ecf0f1")
    title_label.pack(pady=15)

    # Instructions
    instructions = tk.Label(window, text="Guess a number between 1 and 100", font=("Arial", 12),
                            bg="#2c3e50", fg="#bdc3c7")
    instructions.pack(pady=5)

    # Result Label
    label_result = tk.Label(window, text="Click 'New Game' to start!", font=("Arial", 12),
                            bg="#2c3e50", fg="#ecf0f1", wraplength=350)
    label_result.pack(pady=10)

    # Attempts Left
    label_attempts = tk.Label(window, text=f"Attempts left: {max_attempts}", font=("Arial", 10),
                              bg="#2c3e50", fg="#95a5a6")
    label_attempts.pack(pady=5)

    # Entry
    entry_guess = tk.Entry(window, font=("Arial", 14), width=10, justify="center", bg="#ecf0f1", fg="#2c3e50")
    entry_guess.pack(pady=10)
    entry_guess.bind("<Return>", on_enter_key)

    # Buttons
    button_guess = tk.Button(window, text="Make Guess", font=("Arial", 12),
                             command=make_guess, bg="#2980b9", fg="white", width=14)
    button_guess.pack(pady=5)

    button_new = tk.Button(window, text="New Game", font=("Arial", 12),
                           command=start_new_game, bg="#27ae60", fg="white", width=14)
    button_new.pack(pady=5)

    button_quit = tk.Button(window, text="Quit", font=("Arial", 12),
                            command=window.quit, bg="#c0392b", fg="white", width=14)
    button_quit.pack(pady=5)

    return window

def main():
    """Main function to run the game"""
    window = create_window()
    start_new_game()
    window.mainloop()

if __name__ == "__main__":
    main()
