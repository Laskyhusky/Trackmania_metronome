import datetime as date
import tkinter as tk
import json
import time
from playsound3 import playsound



## Class to create the Skeleton of the App with all page switches
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        ## Setting display ratio of the App
        self.geometry("300x500")
        ## Name of the App
        self.title("Launchpage")

        self.play_button = tk.Button(self.master, text="Play", command=self.play_sound)
        self.play_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_sound)
        self.stop_button.pack()

        self.bpm_up_button = tk.Button(self.master, text="BPM up", command=self.bpm_up)
        self.bpm_up_button.pack()

        self.bpm_down_button = tk.Button(self.master, text="BPM down", command=self.bpm_down)
        self.bpm_down_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.sound_playing = False
        self.tick_rate = 1
        self.last_tick = time.perf_counter()



    def play_sound(self):
        if not self.sound_playing:
            self.sound_playing = True
            self.last_tick = time.perf_counter()
            self.give_tick()


    def stop_sound(self):
        self.sound_playing = False


    def give_tick(self):
        if self.sound_playing:
            current_time = time.perf_counter()

            if current_time - self.last_tick >= self.tick_rate:
                print(current_time - self.last_tick)
                playsound("assets/ticksound.mp3", block=False)
                self.last_tick = current_time

            self.after(1, self.give_tick)

    def bpm_up(self):
        if self.tick_rate < 0.3:
            pass
        else:
            self.tick_rate -= 0.1

    def bpm_down(self):
        self.tick_rate += 0.1

    def reset(self):
        self.play_sound()


if __name__ == "__main__":
    app = App()
    app.mainloop()