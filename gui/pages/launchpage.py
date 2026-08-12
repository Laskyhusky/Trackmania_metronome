import datetime as date
import tkinter as tk
import json


## Class to create the Skeleton of the App with all page switches
class Launch_Page(tk.Tk):
    def __init__(self):
        super().__init__()
        ## Setting display ratio of the App
        self.geometry("300x500")
        ## Name of the App
        self.title("Launchpage")

        self.play_button = tk.Button(self.master, text="Play")
        self.play_button.pack()