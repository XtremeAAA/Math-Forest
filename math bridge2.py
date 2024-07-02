import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
from PIL import Image, ImageTk


# The `MathBridge` class is a subclass of `tk.Tk` with a title set to "Math Bridge".
class MathBridge(tk.Tk):
    def __init__(root):
        super().__init__()

        root.title("Math Bridge")

        # Make the window in the default application size
        root.geometry("1280x800")
        root.minsize(width=1280, height=800)
        root.create_welcome_screen()
        root.config(bg="#142948")

    def create_welcome_screen(root):
        for child in root.winfo_children():
            child.destroy()

        root.math_quest_image = PhotoImage(file=r"Icons2/Math Bridge.png")
        root.label = tk.Label(root, image=root.math_quest_image)
        root.label.pack(pady=30)

        # Create gamemode buttons
        root.time_limit_button_image = PhotoImage(
            file=r"Icons2/button_time-limit-game-mode.png"
        )
        root.start_time_limit_button = tk.Button(
            root, command=root.start_time_limit_game, image=root.time_limit_button_image
        )
        root.start_time_limit_button.pack(pady=(200, 0))

        root.score_gm_button_image = PhotoImage(
            file=r"Icons2/button_score-game-mode.png"
        )
        root.start_score_gm_button = tk.Button(
            root,
            command=root.start_score_limit_game,
            image=root.score_gm_button_image,
        )
        root.start_score_gm_button.pack(pady=(20, 0))

        # Create a button widget to exit full screen mode
        root.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        root.exit_button = tk.Button(
            root,
            text="Return to original screen size",
            command=root.exit_full_screen,
            image=root.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        root.exit_button.place(x=exit_button_x, y=exit_button_y)

    def start_time_limit_game(root):
        # Clear the screen
        for child in root.winfo_children():
            child.destroy()
        # Set score
        global score
        score = 0
        # Original screen size

        root.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        root.exit_button = tk.Button(
            root,
            text="Return to original screen size",
            command=root.exit_full_screen,
            image=root.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        root.exit_button.place(x=exit_button_x, y=exit_button_y)

        # Home button
        root.home_button_img = PhotoImage(file=r"Icons2/button_home.png")
        root.home_button = tk.Button(
            root, text="Home", command=root.show_home_screen, image=root.home_button_img
        )
        home_x = 1080
        home_y = 700
        root.home_button.place(x=home_x, y=home_y)

        # Get ready label
        root.get_ready_label = tk.Label(
            root, text="Get Ready!!", font=("Tahoma", 40), background="#142948"
        )
        root.get_ready_label.pack(pady=30)
        root.after(1000, root.get_ready_label.forget)
        root.after(1000, root.time_limit_countdown)

    def time_limit_countdown(root):
        time_limit_countdown = 4

        def update_countdown():
            nonlocal time_limit_countdown
            if time_limit_countdown > 1:
                time_limit_countdown -= 1
                root.time_limit_countdown_lbl.config(text=time_limit_countdown)
                root.time_limit_countdown_lbl.after(1000, update_countdown)
            else:
                root.time_limit_game_begin()

        root.time_limit_countdown_lbl = tk.Label(
            root, text=time_limit_countdown, font=("Tahoma", 30), background="#142948"
        )
        root.time_limit_countdown_lbl.pack(pady=30)
        update_countdown()

    def time_limit_game_begin(root):
        for child in root.winfo_children():
            child.destroy()

        root.home_button_img = PhotoImage(file=r"Icons2/button_home.png")
        root.home_button = tk.Button(
            root, text="Home", command=root.show_home_screen, image=root.home_button_img
        )
        home_x = 1080
        home_y = 700
        root.home_button.place(x=home_x, y=home_y)

        root.original_screen_size = PhotoImage(
            file=r"Icons2/button_original-screen-size.png"
        )
        root.exit_button = tk.Button(
            root,
            text="Return to original screen size",
            command=root.exit_full_screen,
            image=root.original_screen_size,
        )
        exit_button_x = 30
        exit_button_y = 700
        root.exit_button.place(x=exit_button_x, y=exit_button_y)

        root.time_limit_banner = PhotoImage(file=r"Icons2/Time Limit Game.png")
        root.time_limit_banner_label = tk.Label(root, image=root.time_limit_banner)
        root.time_limit_banner_label.pack(pady=30)
        root.time_limit_question()
        root.score_def()
        root.time_limit_countdown_180()
        
        root.characters = [  # Resize the image to 100x100
            ImageTk.PhotoImage(Image.open("characters/Character stage 5.png").resize((191, 225))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 4.png").resize((137, 224))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 3.png").resize((96, 135))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 2.png").resize((83, 103))),
            ImageTk.PhotoImage(Image.open("characters/Character stage 1.png").resize((49, 100))),
        ]
        
        root.character_index = 0
        root.character_lbl = tk.Label(root, image=root.characters[root.character_index])
        root.character_lbl.place(relx=0.5, y=660, anchor="center")
        root.time_limit_countdown_180()

    def score_def(root):
        global score
        root.score_lbl = tk.Label(
            root,
            text=f"Score = {score}",
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        root.score_lbl.place(x=70, y=100)

    def time_limit_question(root):
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
        root.display_question()
        root.tl_user_input()
        root.tl_submit_answer_button()

    def display_question(root):
        root.question_text_lbl = tk.Label(
            root, text=question_text, font=("Tahoma", 40), background="#142948"
        )
        root.question_text_lbl.pack(pady=(180, 0))

    def tl_submit_answer_button(root):
        root.tl_submit_answer_png = PhotoImage(file=r"Icons2/button_submit-answer.png")
        root.tl_submit_button = tk.Button(
            root,
            command=root.tl_check_answer,
            image=root.tl_submit_answer_png,
            background="#142948",
        )
        root.tl_submit_button.place(x=555, y=450)

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

    def tl_user_input(root):
        global tl_user_input
        """Create an Entry widget with validation to only allow numbers and a single full stop."""

        tl_user_input = tk.Entry(
            root,
            width=60,
            justify="center",
        )
        tl_user_input.pack()
        tl_user_input.focus_set()  # Set the focus to the Entry widget
        root.x2dp_test = tk.Label(
            root,
            text=x2dp,
            font=("Tahoma", 30),
            background="#142948",
            fg="#EE4B2B",  # the red text colour
        )
        root.x2dp_test.place(x=70, y=160)
        root.bind("<Return>", lambda event: root.tl_check_answer())


    def validate_input(root, input_string):  # noqa: F811
        if input_string.count(".") != 1:
            return False
        
        parts = input_string.split(".")
        for part in parts:
            if not part.isdigit():
                return False
        
        if len(parts[1]) != 2:
            return False
        
        return True

    def tl_check_answer(root, event=None):
        global tl_user_input
        global x2dp
        global score

        user_answer = tl_user_input.get()  # Get the user's input

        if not root.validate_input(user_answer):
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
            root.score_lbl.config(text=f"Score = {score}")  # Update the score label
            tl_user_input.pack_forget()
            root.question_text_lbl.pack_forget()
            root.time_limit_question()  # Generate a new question
        else:
            tl_user_input.pack_forget()
            root.question_text_lbl.pack_forget()
            root.time_limit_question()  # Generate a new question

    def time_limit_countdown_180(root):
        time_limit_countdown_180 = 180
        characters = ["character1", "character2", "character3", "character4", "character5"]  # list of characters
        character_index = 0

        def update_countdown_180():
            nonlocal time_limit_countdown_180
            nonlocal character_index
            if time_limit_countdown_180 > 1:
                time_limit_countdown_180 -= 1
                root.time_limit_countdown_180_lbl.config(text=f"{time_limit_countdown_180:03d}")  # Update the label text with leading zeros
                root.time_limit_countdown_180_lbl.after(1000, update_countdown_180)
                if time_limit_countdown_180 % 36 == 0:
                    character_index = (character_index + 1) % len(characters)
                    root.character_lbl.destroy()  # Destroy the old character label
                    root.character_lbl = tk.Label(root, image=root.characters[character_index])
                    root.character_lbl.place(relx=0.5, y=660, anchor="center")  # Create a new character label
            else:
                for child in root.winfo_children():
                    child.destroy()

        #style = ttk.Style()
        #style.configure('time_limit_countdown_180.TLabel', font=('Helvetica', 24, 'bold'), background='#142948', foreground='white')

        #root.time_limit_countdown_180_lbl = ttk.Label(root, text=str(time_limit_countdown_180), style='time_limit_countdown_180.TLabel')
        root.time_limit_countdown_180_lbl = tk.Label(
            root,
            text=time_limit_countdown_180,
            font=("Tahoma", 30),
            background="#142948",
        )
        root.time_limit_countdown_180_lbl.place(relx=0.5, y=150, anchor="center")

        update_countdown_180()
        


    def start_score_limit_game(root):
        for child in root.winfo_children():
            child.destroy()
        
    def show_home_screen(root):
        root.create_welcome_screen()

    def exit_full_screen(root):
        # Remove the full screen attribute
        root.attributes("-fullscreen", False)

        # Resize the window to its previous size
        root.geometry("1280x800")


if __name__ == "__main__":
    app = MathBridge()
    app.mainloop()
