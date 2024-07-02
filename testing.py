import time
import tkinter as tk
from tkinter import Frame, Label, PhotoImage, Place, messagebox
from PIL import Image, ImageTk
import random


class MathQuest(tk.Tk):
    def __init__(root):
        super().__init__()

        root.title("Math Quest")

        # Make the window in the default application size
        root.geometry("1280x800")
        root.minsize(width=1280, height=800)
        root.create_welcome_screen()
        root.config(bg='#558fe6')

    def create_welcome_screen(root):
        for child in root.winfo_children():
            child.destroy()
        # Create welcome text
        root.math_quest_image = PhotoImage(file=r"Icons/Math Quest title (1).png")
        root.label = tk.Label(root, image = root.math_quest_image)
        root.label.pack(pady=30)
        

        # Create gamemode buttons
        root.time_limit_button_image = PhotoImage(file=r"Icons/button_time-limit-game.png")
        root.start_time_limit_button = tk.Button(root, command=root.start_time_limit_game, image = root.time_limit_button_image)
        start_time_limit_game_x = 550
        start_time_limit_game_y = 400
        root.start_time_limit_button.place(x=start_time_limit_game_x, y=start_time_limit_game_y)

        root.score_limit_button_image = PhotoImage(file=r"Icons/button_score-limit-game.png")
        root.start_score_limit_button = tk.Button(root, command=root.start_score_limit_game, image = root.score_limit_button_image)
        start_score_limit_game_x = 550
        start_score_limit_game_y = 340
        root.start_score_limit_button.place(x=start_score_limit_game_x, y=start_score_limit_game_y)

        # Create a button widget to exit full screen mode
        root.original_screen_size = PhotoImage(file=r"Icons/button_original-screen-size.png")
        root.exit_button = tk.Button(root, text="Return to original screen size", command=root.exit_full_screen, image = root.original_screen_size)
        exit_button_x = 30
        exit_button_y = 725
        root.exit_button.place(x=exit_button_x, y=exit_button_y)
    
    def start_score_limit_game(root):
        root.label.pack_forget()
        root.start_time_limit_button.destroy()

    def start_time_limit_game(root):
        # Clear the screen
        for child in root.winfo_children():
            child.destroy()
        
        # Original screen size
        root.original_screen_size = PhotoImage(file=r"Icons/button_original-screen-size.png")
        root.exit_button = tk.Button(root, text="Return to original screen size", command=root.exit_full_screen, image = root.original_screen_size)
        exit_button_x = 30
        exit_button_y = 725
        root.exit_button.place(x=exit_button_x, y=exit_button_y)

        # Home button
        root.home_button_img = PhotoImage(file=r"Icons/button_home (5).png")
        root.home_button = tk.Button(root, text="Home", command=root.show_home_screen, image = root.home_button_img)
        home_x = 1080
        home_y = 725
        root.home_button.place(x=home_x, y=home_y)

        # Get ready label
        root.get_ready_label = tk.Label(root, text="Get Ready!!", font=("Tahoma", 40), background='#558fe6')
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
                

        root.time_limit_countdown_lbl = tk.Label(root, text=time_limit_countdown, font=("Tahoma", 30), background='#558fe6')
        root.time_limit_countdown_lbl.pack(pady=30)
        update_countdown()
    
    def time_limit_game_begin(root):
        for child in root.winfo_children():
            child.destroy()
        
        root.home_button_img = PhotoImage(file=r"Icons/button_home (5).png")
        root.home_button = tk.Button(root, text="Home", command=root.show_home_screen, image = root.home_button_img)
        home_x = 1080
        home_y = 725
        root.home_button.place(x=home_x, y=home_y)
        
        root.original_screen_size = PhotoImage(file=r"Icons/button_original-screen-size.png")
        root.exit_button = tk.Button(root, text="Return to original screen size", command=root.exit_full_screen, image = root.original_screen_size)
        exit_button_x = 30
        exit_button_y = 725
        root.exit_button.place(x=exit_button_x, y=exit_button_y)
        
        root.time_limit_banner = PhotoImage(file=r"Icons/Time Limit Banner.png")
        root.time_limit_banner_label = tk.Label(root, image = root.time_limit_banner)
        root.time_limit_banner_label.pack(pady=30)
            
    def show_home_screen(root):
        root.create_welcome_screen()

    def exit_full_screen(root):
        # Remove the full screen attribute
        root.attributes("-fullscreen", False)

        # Resize the window to its previous size
        root.geometry("1280x800")

if __name__ == "__main__":
    app = MathQuest()
    app.mainloop()