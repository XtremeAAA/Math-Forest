import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
from PIL import Image, ImageTk


# The `MathBridge` class is a subclass of `tk.Tk` with a title set to "Math Bridge".
class MathBridge(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Math Bridge")

        # Make the window in the default application size
        self.geometry("1280x800")
        self.minsize(width=1280, height=800)
        self.create_welcome_screen()
        self.config(bg="#142948")

    def create_welcome_screen(self):
        for child in self.winfo_children():
            child.destroy()

        self.math_quest_image = PhotoImage(file=r"Icons2/Math Bridge.png")
        self.label = tk.Label(self, image=self.math_quest_image)
        self.label.pack(pady=30)

        # Create gamemode buttons
        self.time_limit_button_image = PhotoImage(
            file=r"Icons2/button_time-limit-game-mode.png"
        )
        self.start_time_limit_button = tk.Button(
            self, command=self.start_time_limit_game, image=self.time_limit_button_image
        )
        self.start_time_limit_button.pack(pady=(200, 0))

        self.score_gm_button_image = PhotoImage(
            file=r"Icons2/button_score-game-mode.png"
        )
        self.start_score_gm_button = tk.Button(
            self,
            command=self.start_score_limit_game,
            image=self.score_gm_button_image,
        )
        self.start_score_gm_button.pack(pady=(20, 0))

        # Create a button widget to exit full screen mode
        self.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        self.exit_button = tk.Button(
            self,
            text="Return to original screen size",
            command=self.exit_full_screen,
            image=self.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        self.exit_button.place(x=exit_button_x, y=exit_button_y)

    def start_time_limit_game(self):
        # Clear the screen
        for child in self.winfo_children():
            child.destroy()
        # Set score
        global score
        score = 0
        # Original screen size

        self.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        self.exit_button = tk.Button(
            self,
            text="Return to original screen size",
            command=self.exit_full_screen,
            image=self.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        self.exit_button.place(x=exit_button_x, y=exit_button_y)

        # Home button
        self.home_button_img = PhotoImage(file=r"Icons2/button_home.png")
        self.home_button = tk.Button(
            self, text="Home", command=self.show_home_screen, image=self.home_button_img
        )
        home_x = 1080
        home_y = 700
        self.home_button.place(x=home_x, y=home_y)

        # Get ready label
        self.get_ready_label = tk.Label(
            self, text="Get Ready!!", font=("Tahoma", 40), background="#142948"
        )
        self.get_ready_label.pack(pady=30)
        self.after(1000, self.get_ready_label.forget)
        self.after(1000, self.time_limit_countdown)

    def time_limit_countdown(self):
        time_limit_countdown = 4

        def update_countdown():
            nonlocal time_limit_countdown
            if time_limit_countdown > 1:
                time_limit_countdown -= 1
                self.time_limit_countdown_lbl.config(text=time_limit_countdown)
                self.time_limit_countdown_lbl.after(1000, update_countdown)
            else:
                self.time_limit_game_begin()

        self.time_limit_countdown_lbl = tk.Label(
            self, text=time_limit_countdown, font=("Tahoma", 30), background="#142948"
        )
        self.time_limit_countdown_lbl.pack(pady=30)
        update_countdown()

    def time_limit_game_begin(self):
        for child in self.winfo_children():
            child.destroy()

        self.home_button_img = PhotoImage(file=r"Icons2/button_home.png")
        self.home_button = tk.Button(
            self, text="Home", command=self.show_home_screen, image=self.home_button_img
        )
        home_x = 1080
        home_y = 700
        self.home_button.place(x=home_x, y=home_y)

        self.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        self.exit_button = tk.Button(
            self,
            text="Return to original screen size",
            command=self.exit_full_screen,
            image=self.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        self.exit_button.place(x=exit_button_x, y=exit_button_y)

        self.time_limit_banner = PhotoImage(file=r"Icons2/Time Limit Game.png")
        self.time_limit_banner_label = tk.Label(self, image=self.time_limit_banner)
        self.time_limit_banner_label.pack(pady=30)
        self.time_limit_question()
        self.score_def()
        self.time_limit_countdown_180()
        
        self.characters = [  # Resize the image to 100x100
            ImageTk.PhotoImage(Image.open("characters/Character stage 5.png").resize((191, 225))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 4.png").resize((137, 224))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 3.png").resize((96, 135))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 2.png").resize((83, 103))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 1.png").resize((49, 100))),
        ]
        
        self.character_index = 0
        self.character_lbl = tk.Label(self, image=self.characters[self.character_index])
        self.character_lbl.place(relx=0.5, y=660, anchor="center")
        self.time_limit_countdown_180()

    def score_def(self):
        global score
        self.score_lbl = tk.Label(
            self,
            text=f"Score = {score}",
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        self.score_lbl.place(x=70, y=100)

    def time_limit_question(self):
        # generates the integers for my questions
        coefficient = random.randint(1, 10)
        constant_1 = random.randint(5, 20)
        constant_2 = random.randint(40, 80)
        # solves the question and arounds it to 2 dp
        x = (constant_2 - constant_1) / coefficient
        global x2dp
        x2dp = round(x, 2)
        # global allows me to call this variable in another function
        global question_text
        # compiles the generated integers into a question
        question_text = f"{coefficient}x + {constant_1} = {constant_2}. What is x?"
        self.display_question()
        self.tl_user_input()
        self.tl_submit_answer_button()

    def display_question(self):
        self.question_text_lbl = tk.Label(
            self, text=question_text, font=("Tahoma", 40), background="#142948"
        )
        self.question_text_lbl.pack(pady=(180, 0))

    def tl_submit_answer_button(self):
        self.tl_submit_answer_png = PhotoImage(file=r"Icons2/button_submit-answer.png")
        self.tl_submit_button = tk.Button(
            self,
            command=self.tl_check_answer,
            image=self.tl_submit_answer_png,
            background="#142948",
        )
        self.tl_submit_button.place(x=555, y=450)

    def validate_input(tl_user_input):
            """Validate the input string to only allow numbers and a single full stop."""
            if tl_user_input.count(".") != 1:
                return False
            
            parts = tl_user_input.split(".")
            for part in parts:
                if not part.isdigit():
                    return False
            
            if len(parts[1]) != 2:
                return False
            
            return True

    def tl_user_input(self):
        global tl_user_input
        """Create an Entry widget with validation to only allow numbers and a single full stop."""

        tl_user_input = tk.Entry(
            self,
            width=60,
            justify="center",
        )
        tl_user_input.pack()
        tl_user_input.focus_set()  # Set the focus to the Entry widget
        self.x2dp_test = tk.Label(
            self,
            text=x2dp,
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        self.x2dp_test.place(x=70, y=160)
        self.bind("<Return>", lambda event: self.tl_check_answer())


    def validate_input(self, input_string):  # noqa: F811
        if input_string.count(".") != 1:
            return False
        
        parts = input_string.split(".")
        for part in parts:
            if not part.isdigit():
                return False
        
        if len(parts[1]) != 2:
            return False
        
        return True

    def tl_check_answer(self, event=None):
        global tl_user_input
        global x2dp
        global score

        user_answer = tl_user_input.get()  # Get the user's input

        if not self.validate_input(user_answer):
            messagebox.showerror("Invalid Input", "Please enter a valid number with two decimal places.")
            tl_user_input.delete(0, 'end')  # Clear the input field
            tl_user_input.focus_set()
            return

        try:
            user_answer = float(user_answer)  # Try to convert the input to a float
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            tl_user_input.delete(0, 'end')  # Clear the input field
            tl_user_input.focus_set()
            return

        if round(user_answer, 2) == x2dp:  # Compare the rounded user's answer to x2dp
            score += 1
            self.score_lbl.config(text=f"Score = {score}")  # Update the score label
            tl_user_input.pack_forget()
            self.question_text_lbl.pack_forget()
            self.time_limit_question()  # Generate a new question
        else:
            tl_user_input.pack_forget()
            self.question_text_lbl.pack_forget()
            self.time_limit_question()  # Generate a new question

    def time_limit_countdown_180(self):
        time_limit_countdown_180 = 180
        characters = ["character1", "character2", "character3", "character4", "character5"]  # list of characters
        character_index = 0

        def update_countdown_180():
            nonlocal time_limit_countdown_180
            nonlocal character_index
            if time_limit_countdown_180 > 1:
                time_limit_countdown_180 -= 1
                self.time_limit_countdown_180_lbl.config(text=f"{time_limit_countdown_180:03d}")  # Update the label text with leading zeros
                self.time_limit_countdown_180_lbl.after(1000, update_countdown_180)
                if time_limit_countdown_180 % 36 == 0:
                    character_index = (character_index + 1) % len(characters)
                    self.character_lbl.destroy()  # Destroy the old character label
                    self.character_lbl = tk.Label(self, image=self.characters[character_index])
                    self.character_lbl.place(relx=0.5, y=660, anchor="center")  # Create a new character label
            else:
                time_limit_end_message = (f"Time limit game mode is over! You finished with a score of {score}.")
                messagebox.showinfo("MathBridge", time_limit_end_message)
                for child in self.winfo_children():
                    child.destroy()
                self.create_welcome_screen()

        self.time_limit_countdown_180_lbl = tk.Label(
            self,
            text=time_limit_countdown_180,
            font=("Tahoma", 30),
            background="#142948",
        )
        self.time_limit_countdown_180_lbl.place(relx=0.5, y=150, anchor="center")

        update_countdown_180()
        




















    def start_score_limit_game(self):
        for child in self.winfo_children():
            child.destroy()

        global sg_score
        sg_score = 0

        self.score_game_banner = PhotoImage(file=r"Icons2/Score Limit Banner.png")
        self.score_game_banner_lbl = tk.Label(self, image=self.score_game_banner)
        self.score_game_banner_lbl.pack(pady=30)

        self.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        self.exit_button = tk.Button(
            self,
            text="Return to original screen size",
            command=self.exit_full_screen,
            image=self.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        self.exit_button.place(x=exit_button_x, y=exit_button_y)

        self.home_button_img = PhotoImage(file=r"Icons2/button_home.png")
        self.home_button = tk.Button(
            self, text="Home", command=self.show_home_screen, image=self.home_button_img
        )
        home_x = 1080
        home_y = 700
        self.home_button.place(x=home_x, y=home_y)
        
        self.sg_score_lbl = tk.Label(
            self,
            text=f"Score = {sg_score}",
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        self.sg_score_lbl.place(x=70, y=100)
        
        self.score_game_question()

    def score_game_question(self):
        # generates the integers for my questions
        coefficient = random.randint(1, 10)
        constant_1 = random.randint(5, 20)
        constant_2 = random.randint(40, 80)
        # solves the question and arounds it to 2 dp
        x = (constant_2 - constant_1) / coefficient
        global x2dp
        x2dp = round(x, 2)
        # global allows me to call this variable in another function
        global question_text
        # compiles the generated integers into a question
        question_text = f"{coefficient}x + {constant_1} = {constant_2}. What is x?"
        self.score_game_display_question()
        self.sg_user_input()
        self.sg_submit_answer_button()

    def score_game_display_question(self):
            self.question_text_lbl = tk.Label(
                self, text=question_text, font=("Tahoma", 40), background="#142948"
            )
            self.question_text_lbl.pack(pady=(180, 0))

    def sg_validate_input(self, user_input):
        """Validate the input string to only allow numbers and a single full stop."""
        if user_input.count(".") != 1:
            return False
        
        parts = user_input.split(".")
        for part in parts:
            if not part.isdigit():
                return False
        
        if len(parts[1]) != 2:
            return False
        
        return True

    def sg_user_input(self):
        self.user_input_entry = tk.Entry(
            self,
            width=60,
            justify="center",
        )
        self.user_input_entry.pack()
        self.user_input_entry.focus_set()  # Set the focus to the Entry widget
        self.x2dp_test = tk.Label(
            self,
            text=x2dp,
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        self.x2dp_test.place(x=70, y=160)
        self.bind("<Return>", lambda event: self.sg_check_answer())


    def sg_submit_answer_button(self):
        self.sg_submit_answer_png = PhotoImage(file=r"Icons2/button_submit-answer.png")
        self.sg_submit_button = tk.Button(
            self,
            command=self.sg_check_answer,
            image=self.sg_submit_answer_png,
            background="#142948",
        )
        self.sg_submit_button.place(x=555, y=450)

    def sg_check_answer(self, event=None):
        global x2dp
        global sg_score

        user_answer = self.user_input_entry.get()  # Get the user's input
        self.sg_score_lbl = tk.Label(
            self,
            text=f"Score = {sg_score}",
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        self.sg_score_lbl.place(x=70, y=100)

        if not self.sg_validate_input(user_answer):
            messagebox.showerror("Invalid Input", "Please enter a valid number with two decimal places.")
            self.user_input_entry.delete(0, 'end')  # Clear the input field
            self.user_input_entry.focus_set()
            return

        try:
            user_answer = float(user_answer)  # Try to convert the input to a float
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            self.user_input_entry.delete(0, 'end')  # Clear the input field
            self.user_input_entry.focus_set()
            return

        if round(user_answer, 2) == x2dp:  # Compare the rounded user's answer to x2dp
            sg_score += 1
            self.sg_score_lbl.config(text=f"Score = {sg_score}")  # Update the score label
            self.user_input_entry.pack_forget()
            self.question_text_lbl.pack_forget()
            self.score_game_question()  # Generate a new question
        else:
            self.user_input_entry.pack_forget()
            self.question_text_lbl.pack_forget()
            self.score_game_question()  # Generate a new question

        
    def show_home_screen(self):
        self.create_welcome_screen()

    def exit_full_screen(self):
        # Remove the full screen attribute
        self.attributes("-fullscreen", False)

        # Resize the window to its previous size
        self.geometry("1280x800")


if __name__ == "__main__":
    app = MathBridge()
    app.mainloop()
