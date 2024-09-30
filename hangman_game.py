import random
import tkinter as tk
from tkinter import messagebox
from word_list import get_random_word

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # Set window dimensions and center it
        window_width = 400
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        root.resizable(False, False)

        # Initialize game variables
        self.word = get_random_word().lower()
        self.word_display = ['_'] * len(self.word)
        self.guesses_left = 6
        self.guessed_letters = set()

        # Setup the interface
        self.setup_ui()

    def setup_ui(self):
        # Title Label (Styled like an h1 element in CSS)
        self.title_label = tk.Label(
            self.root, text="Hangman Game", font=("Helvetica", 24, "bold"), bg="#34495e", fg="white", padx=10, pady=10
        )
        self.title_label.pack(pady=20)

        # Word Display Label (like the word being guessed)
        self.word_label = tk.Label(
            self.root, text=" ".join(self.word_display), font=("Helvetica", 18), bg="#ecf0f1", fg="#2c3e50", padx=5, pady=5
        )
        self.word_label.pack(pady=20)

        # Guess Entry Box
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14), justify="center", width=5, bg="#ecf0f1", fg="#34495e")
        self.guess_entry.pack(pady=10)

        # Guess Button (Styled like a CSS button)
        self.guess_button = tk.Button(
            self.root, text="Guess", font=("Helvetica", 14, "bold"), bg="#1abc9c", fg="white", activebackground="#16a085", width=10,
            command=self.check_guess
        )
        self.guess_button.pack(pady=10)

        # Info Label (for showing incorrect guesses left)
        self.info_label = tk.Label(
            self.root, text=f"Incorrect Guesses Left: {self.guesses_left}", font=("Helvetica", 14), bg="#34495e", fg="white", padx=10, pady=5
        )
        self.info_label.pack(pady=5)

        # Quit Button (Styled for quitting)
        self.quit_button = tk.Button(
            self.root, text="Quit", font=("Helvetica", 14), bg="#e74c3c", fg="white", activebackground="#c0392b", width=10,
            command=self.root.quit
        )
        self.quit_button.pack(pady=20)

        # Styling root background
        self.root.configure(bg="#34495e")  # Dark background color

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You have already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[idx] = letter
        else:
            self.guesses_left -= 1

        self.update_ui()

        if "_" not in self.word_display:
            messagebox.showinfo("You Won!", f"Congratulations! You guessed the word: {self.word}")
            self.reset_game()

        if self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was: {self.word}")
            self.reset_game()

    def update_ui(self):
        self.word_label.config(text=" ".join(self.word_display))
        self.info_label.config(text=f"Incorrect Guesses Left: {self.guesses_left}")

    def reset_game(self):
        self.word = get_random_word().lower()
        self.word_display = ['_'] * len(self.word)
        self.guesses_left = 6
        self.guessed_letters.clear()
        self.update_ui()

# Main Function to Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
