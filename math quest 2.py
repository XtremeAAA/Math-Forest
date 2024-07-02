import tkinter as tk
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quest")

        # Set the window to full-screen mode
        self.root.attributes('-fullscreen', True)

        self.score = 0
        self.time_remaining = 180

        self.create_welcome_screen()

    def create_welcome_screen(self):
        # Initialize the welcome screen with labels and buttons
        self.welcome_label = tk.Label(self.root, text="Welcome to Math Quest", font=("Helvetica", 30))
        self.welcome_label.pack(side='top', fill='both', expand=True)

        self.math_quest_label = tk.Label(self.root, text="Math Quest", font=("Helvetica", 60))
        self.math_quest_label.pack(side='top', fill='both', expand=True)

        self.time_limit_button = tk.Button(self.root, text="Time Limit Game", command=self.start_time_limit_game, font=("Helvetica", 20))
        self.time_limit_button.pack(side='bottom', fill='both', expand=True)
        self.time_limit_button.config(height=1, width=1)

        self.score_game_button = tk.Button(self.root, text="Score Game", command=self.start_score_game, font=("Helvetica", 20))
        self.score_game_button.pack(side='bottom', fill='both', expand=True)


    def start_time_limit_game(self):
        # Initialize the time limit game screen with labels, entry, and buttons
        self.clear_welcome_screen()

        self.get_ready_label = tk.Label(self.root, text="Get ready!", font=("Helvetica", 30))
        self.get_ready_label.pack()

        self.countdown_label = tk.Label(self.root, font=("Helvetica", 20), justify='center')
        self.countdown_label.pack()

        self.question_label = tk.Label(self.root, font=("Helvetica", 40))
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.answer_entry.pack()

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 30))
        self.score_label.pack()

        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.start_time_limit_game, font=("Helvetica", 20))
        self.try_again_button.pack()

        self.home_button = tk.Button(self.root, text="Home", command=self.create_welcome_screen, font=("Helvetica", 20))
        self.home_button.pack()

        self.generate_time_limit_question()

    def start_score_game(self):
        # Initialize the score game screen with labels, entry, and buttons
        self.clear_welcome_screen()

        self.question_label = tk.Label(self.root, font=("Helvetica", 40))
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.answer_entry.pack()

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 30))
        self.score_label.pack()

        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.start_score_game, font=("Helvetica", 20))
        self.try_again_button.pack()

        self.home_button = tk.Button(self.root, text="Home", command=self.create_welcome_screen, font=("Helvetica", 20))
        self.home_button.pack()

        self.generate_score_game_question()

    def generate_time_limit_question(self):
        # Generate a time limit game question and update the question label
        coefficient = random.randint(1, 10)
        constant1 = random.randint(0, 50)
        constant2 = random.randint(50, 500)

        try:
            self.current_answer = constant2 / coefficient
        except ZeroDivisionError:
            messagebox.showerror("Error", "Invalid coefficients. Please try again.")
            self.create_welcome_screen()
            return

        question_text = f"{coefficient}x + {constant1} = {constant2}. What is x?"

        self.question_label.config(text=question_text)
        self.question_label.update()

        self.start_countdown()

    def generate_score_game_question(self):
        # Generate a score game question and update the question label
        coefficient = random.randint(1, 10)
        constant1 = random.randint(0, 50)
        constant2 = random.randint(50, 500)

        try:
            self.current_answer = constant2 / coefficient
        except ZeroDivisionError:
            messagebox.showerror("Error", "Invalid coefficients. Please try again.")
            self.create_welcome_screen()
            return

        question_text = f"{coefficient}x + {constant1} = {constant2}. What is x?"

        self.question_label.config(text=question_text)

    def update_countdown(self):
        # Update the countdown label and check if time is up
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.countdown_label.config(text=f"Time Remaining: {self.time_remaining} s")
            self.root.after(1000, self.update_countdown)
        else:
            self.get_ready_label.pack_forget()  # Hide the "Get ready" label
            self.end_game()

    def start_countdown(self):
        # Hide the question during the countdown
        self.question_label.pack_forget()

        # Start the countdown before the time limit game
        self.countdown_label.config(text="Get ready!", justify='center')
        self.root.update()
        self.root.after(1000, lambda: self.countdown(3))
        self.get_ready_label.pack_forget()

    def countdown(self, seconds):
        if seconds > 0:
            self.countdown_label.config(text=str(seconds), justify='center')
            self.root.update()
            self.root.after(1000, lambda: self.countdown(seconds - 1))
        else:
            self.countdown_label.config(text="Go!", justify='center')
            self.root.after(1000, self.update_countdown)

            # Show the question after the countdown
            self.question_label.pack()

    def end_game(self):
        # Handle the end of the time limit game
        user_answer = self.answer_entry.get()

        try:
            user_answer = float(user_answer)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
            return

        if round(user_answer, 2) == round(self.current_answer, 2):
            self.score += 1
        else:
            self.score -= 1

        self.show_score_animation()

    def show_score_animation(self):
        # Show the score animation and generate a new time limit question
        self.score_label.config(text=f"Score: {self.score}")
        self.score_label.update()

        for i in range(5, 0, -1):
            self.score_label.config(text=f"Score: {self.score} - Next question in {i} seconds")
            self.score_label.update()
            self.root.after(500, self.root.update)

        self.generate_time_limit_question()

    def clear_welcome_screen(self):
        # Clear the welcome screen widgets
        self.welcome_label.destroy()
        self.math_quest_label.destroy()
        self.time_limit_button.destroy()
        self.score_game_button.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    math_game = MathGame(root)
    root.mainloop()